# Parametric Guitar Designer

A workflow tool that bridges AI image generation and engineering precision for instrument body design.

## What this is

This repository will house a workflow tool for designing instrument body shapes without requiring CAD expertise. The tool addresses a specific gap in the design process: AI image generators produce visually compelling guitar concepts but no usable dimensions, while parametric CAD packages require designers to know what they want before they start designing.

The workflow proceeds through three stages:

**Stage 1 — Visual ideation.** Generate or import an AI-produced image of an instrument body. The image captures the visual character of the design but has no dimensional reality.

**Stage 2 — Dimensional grounding.** Sketch the body in a browser-based editor that produces real dimensions: body length, lower bout width, upper bout width, waist, depth, and proportional relationships. The sketch can be developed independently or traced over the AI image as reference.

**Stage 3 — Calibration and refinement.** Map the sketch dimensions onto the AI image to give the visual concept dimensional reality. Apply proportional design methodology to refine the design until it is internally coherent. Export a calibrated specification ready for CAD work.

The output is a graphic image with documented dimensions, suitable for taking into Fusion 360 or another CAD package as a reference for the precision modeling that produces buildable files. The tool does not replace CAD; it precedes CAD.

## Why this approach exists

Three problems with existing instrument body design workflows motivate this tool:

**Pure CAD requires you to know what you want before you start.** Parametric tools like Fusion 360 are powerful for refining known designs, but the constraint and parameter overhead slows down early-stage exploration. A designer who is still discovering what the body should look like spends more time managing CAD than exploring options.

**AI image generation produces inspiration without specifications.** A compelling generated image of a guitar body is visually motivating but cannot be built. Without dimensions, the image cannot transition into manufacturing, CAM toolpaths, or even basic builder-grade plans.

**Pure sketching tools lack instrument-specific intelligence.** Generic vector graphics editors can produce shapes but offer no guidance about whether the shape makes sense as an instrument. Proportions, ergonomics, and acoustic implications are invisible to tools that treat a guitar body as just another curve.

This tool combines AI ideation, sketching with dimensions, and proportional design refinement into a single workflow that addresses all three problems together.

## Who this is for

The intended user is anyone designing instrument bodies who needs more than a sketch but less than full parametric CAD:

- Working luthiers exploring new body shapes before committing to CAD modeling
- Lutherie students learning instrument design without yet having CAD expertise
- Custom shop designers iterating on customer requests
- Amateur builders wanting to design their own instruments
- Instrument modifiers planning custom bodies for existing necks and electronics

The tool serves the design exploration phase. Users who already have well-developed designs and need precision specifications will continue to use CAD packages directly. Users who are still discovering what they want to build will find the workflow faster than CAD and more useful than pure sketching.

## What it produces

The deliverable from this workflow is a calibrated design specification suitable for handoff to CAD or for direct use as builder reference material:

- Vector graphic of the body outline at correct scale
- Dimensional callouts for key measurements
- Reference to the AI image that informed the visual character
- Proportional analysis showing how the design relates to established instrument design principles
- Notes captured during the design process

The specification is not a buildable CAD file. It is an organized starting point for the precision work that follows. A user with CAD skills imports the specification as a reference layer in Fusion 360 (or equivalent) and produces the manufacturing-grade model. A user without CAD skills can take the specification to a CAD-capable collaborator with confidence that the design intent is documented.

## Current status

The repository is currently a skeleton. The workflow described above is the design intent for the eventual product. Implementation has not yet begun.

The components that will be assembled into this workflow exist in various forms within the broader Production Shop platform. The Body Outline Editor sketching tool exists. The proportional design methodology exists. The AI image generation step uses external tools (Midjourney, DALL-E, Stable Diffusion) accessed through their respective interfaces. The work to integrate these components into a coherent workflow tool is scheduled for later development, after foundational lutherie infrastructure is operational.

This README captures the design intent so that future development can proceed against a documented goal rather than reconstructing the concept from memory.

## How this fits the broader platform

The Production Shop is an integrated platform for working luthiers. The Parametric Guitar Designer described here is one tool within that platform, not a separate product. When the platform's web property launches, this tool will be presented as a feature of the Production Shop rather than as a standalone application with its own domain.

The workflow this tool implements emerged from actual use during the Smart Guitar design process. The designer needed dimensional grounding for an AI-generated visual concept and discovered that combining sketching, AI imagery, and proportional methodology produced a workable design faster than any single approach alone. The tool exists to make that workflow available to other designers facing similar problems.

## Repository structure

```
ltb-parametric-guitar/
├── client/          # Browser-based sketching and visualization (Vue 3, planned)
├── server/          # Backend API for dimension calculation, image processing,
│                    # and proportional analysis (FastAPI)
├── docs/            # Design documentation and methodology references (planned)
└── README.md        # This document
```

The client provides the sketching interface and visualization. The server provides backend computation for dimensional analysis, image calibration, proportional verification, and export generation. The two communicate through a REST API that will be documented as the implementation develops.

## Related work

The Production Shop platform includes related tools that operate at different stages of the instrument design and production process:

- Wood database with verified species characterization for material selection
- Acoustic studio tools for soundhole and bracing design
- CAM toolpath generation for CNC fabrication
- Fretboard ecosphere for neck and fret design
- Bridge designer for saddle compensation and intonation

The Parametric Guitar Designer focuses specifically on body shape design, complementing rather than replacing these other tools. A complete instrument design workflow uses multiple Production Shop tools in sequence, with the Parametric Guitar Designer typically near the beginning of that sequence.

## License

Copyright © 2026 Texas Guitar Exchange LLC. All rights reserved.

Licensing terms for eventual public release will be determined when the tool is ready for broader availability. The current repository represents private development of platform infrastructure.
