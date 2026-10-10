check:
    uv run --locked --offline python scripts/check_repository.py
    uv run --locked --offline python scripts/check_distribution.py
    uv run --locked --offline python -m unittest discover -s tests -v

demo profile=".local/engines.json":
    uv run --locked --offline python scripts/rover_demo.py --profile {{quote(profile)}}

configure opensysml toolkit lsp library:
    uv run --locked --offline python scripts/configure_engines.py --opensysml {{quote(opensysml)}} --toolkit {{quote(toolkit)}} --opensysml-lsp {{quote(lsp)}} --library {{quote(library)}}

visual-demo output=".local/visualization-demo/energy.svg":
    uv run --locked --offline python skills/mbse-excalidraw/scripts/scene_check.py examples/visualization/rover-energy.excalidraw
    uv run --locked --offline python skills/mbse-engineering-plots/scripts/plot_energy.py examples/rover/evidence/summary.json {{quote(output)}} --reserve 0.2

sync-version:
    uv run --locked --offline python scripts/check_distribution.py --sync-version

onboarding-demo destination=".local/team-onboarding":
    uv run --locked --offline python scripts/onboarding_demo.py {{quote(destination)}}
