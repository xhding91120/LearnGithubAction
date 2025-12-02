# Hello World - GitHub Actions Demo

A simple Python "Hello World" project with GitHub Actions workflows.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       ├── hello-world.yml    # Basic workflow demo
│       └── python-ci.yml      # Python CI/CD workflow
├── hello.py                   # Main Python script
├── test_hello.py              # Unit tests
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Local Development

### Run the application
```bash
python hello.py
```

### Run tests
```bash
python -m unittest test_hello.py -v
```

## GitHub Actions Workflows

### 1. Hello World Workflow (`.github/workflows/hello-world.yml`)
- Demonstrates basic GitHub Actions syntax
- Runs on every push, pull request, or manual trigger
- Displays repository and system information

### 2. Python CI Workflow (`.github/workflows/python-ci.yml`)
- Tests the Python code across multiple Python versions (3.9-3.12)
- Installs dependencies from `requirements.txt`
- Runs unit tests
- Executes the application

## Getting Started with GitHub Actions

1. **Push this code to GitHub.com**
   ```bash
   git init
   git add .
   git commit -m "Initial commit with GitHub Actions"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **View workflow runs**
   - Go to your repository on GitHub.com
   - Click the **Actions** tab
   - Watch your workflows run automatically!

3. **Manual trigger**
   - In the Actions tab, select a workflow
   - Click **Run workflow** button
   - Choose the branch and click **Run workflow**

## What Happens in GitHub Actions?

When you push code:
1. GitHub detects the workflow files in `.github/workflows/`
2. Spins up a virtual machine (Ubuntu Linux by default)
3. Checks out your code
4. Runs each step defined in the workflow
5. Shows you the results in the Actions tab

## Next Steps

- Modify `hello.py` and push to see the workflow run
- Add more tests to `test_hello.py`
- Try breaking a test to see how failures appear
- Explore the workflow logs in the Actions tab
- Add more jobs or steps to the workflows

## Free Usage

Public repositories get **unlimited** GitHub Actions minutes for free!
