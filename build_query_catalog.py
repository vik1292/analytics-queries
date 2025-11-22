#!/usr/bin/env python3
"""
Query Catalog Builder

Automatically generates or updates the query_catalog.md file by scanning
the sql/ and sas/ directories and extracting metadata from query files.
"""

import os
from pathlib import Path
from datetime import datetime


def extract_yaml_metadata(file_path):
    """Extract YAML metadata from query file headers."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Check if file has YAML front matter (between --- delimiters)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1].strip()
            return parse_simple_yaml(yaml_content)

    return None


def parse_simple_yaml(yaml_str):
    """Simple YAML parser for basic key-value pairs and lists."""
    metadata = {}
    lines = yaml_str.split('\n')
    current_key = None
    current_list = []

    for line in lines:
        line = line.rstrip()

        # Skip empty lines
        if not line.strip():
            continue

        # Check if it's a list item
        if line.strip().startswith('- '):
            if current_key:
                current_list.append(line.strip()[2:].strip())
        else:
            # Save previous list if exists
            if current_key and current_list:
                metadata[current_key] = current_list
                current_list = []
                current_key = None

            # Parse key-value pair
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")

                if value:
                    # It's a direct key-value pair
                    metadata[key] = value
                else:
                    # It might be a list that follows
                    current_key = key
                    current_list = []

    # Save last list if exists
    if current_key and current_list:
        metadata[current_key] = current_list

    return metadata


def build_catalog():
    """Build the query catalog from SQL and SAS files."""
    base_dir = Path(__file__).parent.parent
    catalog_path = base_dir / 'docs' / 'query_catalog.md'

    # Define source directories and their file extensions
    source_dirs = [
        ('sql', '*.sql', 'SQL'),
        ('sas', '*.sas', 'SAS')
    ]

    categories = {
        'IVR Queries': 'ivr',
        'Agent Queries': 'agent',
        'Collections Queries': 'collections'
    }

    catalog_content = "# Analytics Query Catalog\n\n"
    catalog_content += "This catalog provides an index of all available queries organized by category and source system.\n\n"
    catalog_content += "## Table of Contents\n\n"
    for category_name in categories.keys():
        catalog_content += f"- [{category_name}](#{category_name.lower().replace(' ', '-')})\n"
    catalog_content += "\n---\n\n"

    # Process each category
    for category_name, folder_name in categories.items():
        catalog_content += f"## {category_name}\n\n"

        # Track if we found any queries in this category
        found_queries = False

        # Process each source directory (sql and sas)
        for source_dir, pattern, source_label in source_dirs:
            query_dir = base_dir / source_dir / folder_name

            if query_dir.exists():
                query_files = sorted(query_dir.glob(pattern))

                if query_files:
                    found_queries = True
                    catalog_content += f"### {source_label} Queries\n\n"

                    for query_file in query_files:
                        rel_path = query_file.relative_to(base_dir)
                        metadata = extract_yaml_metadata(query_file)

                        if metadata:
                            # Extract metadata fields
                            query_id = metadata.get('id', 'N/A')
                            name = metadata.get('name', query_file.name)
                            business_question = metadata.get('business_question', 'No business question available')
                            tags = metadata.get('tags', [])
                            source_system = metadata.get('source_system', 'N/A')
                            grain = metadata.get('grain', 'N/A')
                            owner_team = metadata.get('owner_team', 'N/A')
                            last_validated = metadata.get('last_validated', 'N/A')

                            # Build query entry
                            catalog_content += f"#### [{name}](../{rel_path})\n\n"
                            catalog_content += f"**Business Question:** {business_question}\n\n"
                            catalog_content += f"**Details:**\n"
                            catalog_content += f"- **ID:** `{query_id}`\n"
                            catalog_content += f"- **Source System:** {source_system}\n"
                            catalog_content += f"- **Grain:** {grain}\n"
                            catalog_content += f"- **Owner Team:** {owner_team}\n"
                            catalog_content += f"- **Last Validated:** {last_validated}\n"

                            if tags:
                                tags_str = ', '.join([f"`{tag}`" for tag in tags])
                                catalog_content += f"- **Tags:** {tags_str}\n"

                            catalog_content += "\n"
                        else:
                            # Fallback if no metadata found
                            catalog_content += f"#### [{query_file.name}](../{rel_path})\n"
                            catalog_content += f"*No metadata available*\n\n"

                    catalog_content += "\n"

        if not found_queries:
            catalog_content += "*No queries found in this category*\n\n"

    catalog_content += "---\n\n"
    catalog_content += f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

    # Ensure docs directory exists
    docs_dir = base_dir / 'docs'
    docs_dir.mkdir(exist_ok=True)

    with open(catalog_path, 'w') as f:
        f.write(catalog_content)

    print(f"✓ Catalog generated at {catalog_path}")


if __name__ == '__main__':
    build_catalog()
