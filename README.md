# SPAIS website

The website of the **Sustainable Physical AI Society at the University of Waterloo**.

**Bringing AI into the real world for a sustainable future.**


## Included

- Responsive home and agricultural robotics project pages.
- Black, white, and silver visual design with the original SPAIS team cover photo.
- Mobile navigation, photo albums, team disclosures, and contact tabs.
- Local image assets, with provenance in [PHOTO_SOURCES.md](PHOTO_SOURCES.md).
- GitHub Pages deployment on pushes to `main`, plus manual deployment.

The website is plain HTML, CSS, and JavaScript. It has no npm dependencies, database, or backend. Contact actions open email, Discord, or the society's social channels; the site does not collect form submissions. The robotics page describes a proposed project and prototype goals.

## Publish with GitHub Pages

1. Create a GitHub repository, for example `spais-website`, with a `main` branch. For GitHub Free, use a public repository for Pages.
2. Upload the **contents** of this folder, including `.github/workflows/pages.yml`, to the repository root. `index.html` must be at the root. Do not upload only the ZIP or add an extra enclosing folder.
3. In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. The workflow is already included; no starter template is needed.
4. Open **Actions → Deploy SPAIS to GitHub Pages → Run workflow** and select `main`. The published URL appears in the deployment and Pages settings.

Once enabled, subsequent pushes to `main` automatically deploy. If the first run happened before Pages was enabled, rerun it after step 3. No personal access token needs to be stored in this project for the included workflow.

GitHub Pages normally publishes a public website. The package contains source files only; preparing or downloading it does not create a repository or publish a site.

The workflow packages only the website into `_site/`. Python updates canonical and Open Graph URLs from the real Pages address, including repository subpaths and an already-configured custom domain. You do not have to enter a GitHub username in the HTML.

## Preview locally

From this folder, with Python 3 installed:

```sh
python3 -m http.server 8000
```

On Windows, use `py -m http.server 8000` if `python3` is not available. Open <http://localhost:8000/>. Press `Ctrl+C` to stop.

## Edit the site

| File | Purpose |
| --- | --- |
| `index.html` | Home page copy, sections, team descriptions, and contact links |
| `project.html` | Agricultural robotics concept, research questions, and roadmap |
| `assets/styles.css` | Colours, layout, typography, and responsive behaviour |
| `assets/app.js` | Navigation, contact tabs, photo albums, and image captions |
| `assets/team-cover.jpg` | Main team cover photo |
| `assets/platform-concept.svg` | Illustrative robot concept |
| `tools/build_pages.py` | Deployment packaging and absolute sharing URLs |
| `.github/workflows/pages.yml` | GitHub Actions deployment workflow |

Navigation and footer markup are present in both HTML pages; update both when changing shared links. When replacing a photograph, update its alt text in HTML or album caption in `app.js` as appropriate. If the filename is unchanged, the image references do not need to change.

To inspect the deployment output locally:

```sh
# Example address for local verification; replace with your actual published URL.
python3 tools/build_pages.py --base-url https://YOUR_USERNAME.github.io/spais-website/
python3 -m http.server 8001 --directory _site
```

`_site/` is generated and ignored by Git. Do not edit it directly. If adding another HTML page, add it and its sharing image to `PAGES` in `tools/build_pages.py` so that it is included in deployment.

## Reference

- [GitHub: configuring a Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub: using custom workflows with Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

This package is supplied for SPAIS website maintenance. No open-source licence has been selected for the website or its photographs.
