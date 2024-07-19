# PAS (Produce Administer Submit) Project

This FastAPI project integrates Notion, YouTube, and Claude APIs to automate content creation and management workflows. It provides both API endpoints and CLI tools for seamless interaction with these services.

## Features

- Fetch and create content in Notion
- Upload and manage videos on YouTube
- Generate and refine content using Claude AI
- RESTful API endpoints for service integration
- CLI tools for quick operations

## Prerequisites

- Python 3.8+
- Notion API key
- YouTube API credentials
- Claude API key

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pas-project.git
   cd pas-project
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   NOTION_API_KEY=your_notion_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   CLAUDE_API_KEY=your_claude_api_key
   ```

## Running the Application

### API Server

To start the FastAPI server:

```
uvicorn app.api.main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

### CLI

To use the CLI tools:

```
python -m app.cli.main [command]
```

Available commands:
- `youtube`: Manage YouTube videos
- `notion`: Interact with Notion databases
- `claude`: Generate content using Claude AI

## Usage

[Add detailed usage instructions, including example API calls and CLI commands]

## Testing

To run the test suite:

```
pytest
```

## Architecture Diagram
```
┌─────────────────┐
│    Interface    │
│  (Presentation) │
└────────┬────────┘
         │
┌────────▼────────┐
│   Application   │
│    (Use Cases)  │
└────────┬────────┘
         │
┌────────▼────────┐
│     Domain      │
│ (Business Logic)│
└────────┬────────┘
         │
┌────────▼────────┐
│ Infrastructure  │
│  (Data Sources) │
└─────────────────┘
```

## Role of Each Layer

### Interface Layer (`interface/`)

**Role:** Responsible for interactions with the user interface  
**Components:** API endpoints, CLI commands, GUI (future)  
**Dependencies:** Application Layer  

### Application Layer (`application/`)

**Role:** Coordination and orchestration of use cases  
**Components:** Application services  
**Dependencies:** Domain Layer  

### Domain Layer (`domain/`)

**Role:** Defines business logic and rules  
**Components:** Entities, value objects, domain services, repository interfaces  
**Dependencies:** None (innermost layer)  

### Infrastructure Layer (`infrastructure/`)

**Role:** Interaction with external systems, data access  
**Components:** Repository implementations, external API clients  
**Dependencies:** Domain Layer (implements interfaces)  

### Core (`core/`)

**Role:** Common utilities and configuration  
**Components:** Configuration management, custom exceptions, common utilities  

---

This structure outlines the responsibilities and dependencies of each layer in a clean architecture, ensuring a well-organized and maintainable codebase.

## Contributing

[Add contribution guidelines if applicable]

## License

[Specify the license under which this project is released]