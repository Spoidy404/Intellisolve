# IntelliSolve UML Diagrams

This directory documents the current IntelliSolve implementation.

## Diagram collection

| Diagram | Preview | Editable PlantUML |
|---|---|---|
| Activity | [SVG](ActivityDiagram/ActivityDiagram.svg) | [PUML](ActivityDiagram/ActivityDiagram.puml) |
| Component | [SVG](ComponentDiagram/ComponentDiagram.svg) | [PUML](ComponentDiagram/ComponentDiagram.puml) |
| Sequence | [SVG](SequenceDiagram/SequenceDiagram.svg) | [PUML](SequenceDiagram/SequenceDiagram.puml) |
| Use case | [SVG](UseCaseDiagram/UseCaseDiagram.svg) | [PUML](UseCaseDiagram/UseCaseDiagram.puml) |
| Class / module | [SVG](ClassDiagram/ClassDiagram.svg) | [PUML](ClassDiagram/ClassDiagram.puml) |

## System represented

- **Frontend:** React + TypeScript + Vite. The Home screen provides a canvas with pen, line, rectangle, circle, eraser and text tools, color and brush-size controls, undo/redo/reset, PNG export, and a Run action.
- **HTTP communication:** Axios sends the canvas PNG data URL and `dict_of_vars` to the configured `VITE_API_URL` endpoint at `/calculate`.
- **Backend:** FastAPI exposes a root health response and includes the calculator router under `/calculate`.
- **Request model:** Pydantic `ImageData` contains `image` and `dict_of_vars`.
- **Image handling:** The route Base64-decodes the data URL and opens the image using Pillow.
- **AI processing:** `analyze_image` builds a math/problem-solving prompt with assigned variables and sends the prompt and image to Google's Gemini Generative AI SDK. The returned text is parsed with `ast.literal_eval`.
- **Result rendering:** The route returns a JSON payload; the frontend uses the expression/result values to render draggable MathJax answer overlays.

## Source files inspected

- `inteli-solve-Ai/src/screens/home/index.tsx`
- `inteli-solve-Ai/src/App.tsx`
- `calc-be-main/main.py`
- `calc-be-main/apps/calculator/route.py`
- `calc-be-main/apps/calculator/utils.py`
- `calc-be-main/schema.py`
- `calc-be-main/constants.py`

## Notes

The class diagram uses module/component-style UML because the inspected implementation is primarily functional and does not define a set of domain classes. The Gemini model name shown in the backend source is `gemini-3.5-flash`. The actual API key is read from the environment and is not included in these diagrams. The flow describes the current source implementation; it does not imply additional authentication, persistence, or database services.
