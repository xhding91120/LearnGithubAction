#!/usr/bin/env python3
"""
Simple Hello World Python script
"""

def greet(name="World"):
    """Return a greeting message"""
    return f"Hello, {name}!"

def main():
    """Main function"""
    message = greet()
    print(message)
    print("Welcome to GitHub Actions!")

if __name__ == "__main__":
    main()
