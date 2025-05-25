#!/usr/bin/env python3
"""
Environment Variables Validation Script for GPT Newspaper
This script validates that all required environment variables are properly set.
"""

import os

def load_env_file():
    """Load environment variables from .env file if it exists."""
    env_file = '.env'
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

def validate_env_vars():
    """Validate that all required environment variables are set."""
    
    # Load environment variables from .env file
    load_env_file()
    
    required_vars = {
        'TAVILY_API_KEY': 'Tavily API key for web search functionality',
        'OPENAI_API_KEY': 'OpenAI API key for article generation'
    }
    
    print("🔍 Validating environment variables...\n")
    
    all_valid = True
    
    for var_name, description in required_vars.items():
        value = os.getenv(var_name)
        
        if not value:
            print(f"❌ {var_name}: Not set")
            print(f"   Description: {description}")
            all_valid = False
        elif value.strip() in ['your_tavily_api_key_here', 'your_openai_api_key_here', '<your-tavily-api-key>', '<your-openai-api-key>']:
            print(f"⚠️  {var_name}: Contains placeholder value")
            print(f"   Description: {description}")
            print(f"   Current value: {value}")
            all_valid = False
        else:
            print(f"✅ {var_name}: Set correctly")
        print()
    
    if all_valid:
        print("🎉 All environment variables are properly configured!")
        print("You can now run the GPT Newspaper application.")
    else:
        print("❌ Some environment variables need attention.")
        print("\nTo fix this:")
        print("1. Edit the .env file in the project root")
        print("2. Replace placeholder values with your actual API keys")
        print("3. Save the file and run this script again")
        print("\nAPI key sources:")
        print("- Tavily: https://tavily.com/")
        print("- OpenAI: https://platform.openai.com/")
    
    return all_valid

if __name__ == "__main__":
    validate_env_vars()
