# GitHub Actions Quick Reference

## Workflow Overview

This project uses two GitHub Actions workflows for CI/CD:

### 1. Main CI/CD Pipeline (`.github/workflows/ci-cd.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main`

**Jobs:**
1. **test** - Run tests on Python 3.8, 3.9, 3.10, 3.11, 3.12
2. **docker-test** - Build and test Docker image
3. **release** - Run semantic-release to determine if new version needed
4. **docker-build-and-push** - Build multi-arch images and push to Docker Hub (only on new releases)
5. **security-scan** - Scan published images for vulnerabilities (only on new releases)

### 2. Pull Request Tests (`.github/workflows/pr-test.yml`)

**Triggers:**
- Pull requests to `main` or `develop`

**Jobs:**
1. **test** - Quick tests on Python 3.8 and 3.11
2. **docker-test** - Basic Docker build test

## Deployment Strategy

### Branch Strategy
- **main** - Production releases, Docker images tagged as `latest`
- **develop** - Development branch (if used)
- **feature branches** - Pull request testing only

### Version Strategy
- **Semantic Release** - Automatically determines version based on conventional commits
- **Docker Tags** - Only created when semantic-release creates a new version

**Tags Created**:
- `latest` - Latest stable release from main branch
- `v1.2.3` - Specific version tags
- `1.2` - Major.minor tags
- `1` - Major version tags

## Monitoring

- **Actions Tab** - View workflow runs and logs
- **Security Tab** - View vulnerability scan results
- **Releases** - View automatically created releases
- **Docker Hub** - View published images

## Release Process

1. **Conventional Commits** - Developers use conventional commit format
2. **Merge to Main** - Triggers CI/CD pipeline
3. **Semantic Release** - Analyzes commits and creates release if needed
4. **Docker Deployment** - Only happens if new release was created
5. **Security Scanning** - All published images are scanned

## Commit Impact on Releases

| Commit Type | Version Impact | Example |
|-------------|----------------|---------|
| `feat:` | Minor (1.0.0 → 1.1.0) | `feat: add table support` |
| `fix:` | Patch (1.1.0 → 1.1.1) | `fix: resolve parsing bug` |
| `feat!:` | Major (1.1.1 → 2.0.0) | `feat!: redesign API` |
| `docs:` | Patch (2.0.0 → 2.0.1) | `docs: update readme` |
| `test:` | No release | `test: add unit tests` |
| `chore:` | No release | `chore: update deps` |

For detailed commit guidelines, see [CONTRIBUTING.md](../CONTRIBUTING.md).
