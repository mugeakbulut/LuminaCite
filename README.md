# LuminaCite (V1)

LuminaCite is an advanced academic paper search and visualization system that combines LDA topic modeling with Pennant retrieval to provide intelligent literature discovery.
PS: This platform is an output of the project “Incremental Refinement of Relevance Rankings in Machine Learning-Based Information Retrieval” supported by the 2218 - National Postdoctoral Research Fellowship Program (Project No: 124C132) and hosted by TÜBİTAK ULAKBİM.
Screenshot:

<img width="1449" alt="Ekran Resmi 2025-06-06 11 06 26" src="https://github.com/user-attachments/assets/63980837-5f2e-4777-a8f4-cb4b49a5c5e0" />

## Features

### Advanced Search
- **Intelligent Scoring System**: Combines LDA topic relevance with Pennant access metrics
- **Personalized Results**: Adjustable balance between diversity and relevance
- **Real-time Filtering**: Filter by authors, subjects, and topic categories
- **Multi-language Support**: Turkish and English interface

### Interactive Visualizations
- **Pennant Diagrams**: Visualize papers based on cognitive impact (x-axis) and access ease (y-axis)
- **Topic Distribution Charts**: Interactive radar charts showing topic relationships
- **Sector Analysis**: Papers categorized into Successors (A), Peers (B), and Predecessors (C) sectors

### User Management
- **User Registration/Login**: Secure authentication system
- **Personal Library**: Save and organize favorite papers
- **Research Notes**: Add personal notes to papers

### Modern Interface
- **Responsive Design**: Works on desktop and mobile devices
- **Clean UI**: Intuitive design with soft color coding
- **Interactive Elements**: Hover tooltips and clickable visualizations

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Machine Learning**: scikit-learn (LDA), NLTK
- **Frontend**: HTML5, CSS3, JavaScript, D3.js
- **Styling**: Tailwind CSS

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/KIDR-app.git
   cd KIDR-app
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-login pandas numpy scikit-learn nltk werkzeug
   ```

3. **Download NLTK data**
   ```python
   import nltk
   nltk.download('stopwords')
   ```

4. **Prepare your data**
   - Place your metadata Excel file in the `data/` directory as `metadata.xlsx`
   - Place your citations text file in the `data/` directory as `citations.txt`

5. **Run the application**
   ```bash
   python app.py
   ```
   Or use the provided shell script:
   ```bash
   chmod +x run_app.sh
   ./run_app.sh
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Data Format

### Metadata Excel File
Your `metadata.xlsx` should contain columns like:
- Paper ID
- Title
- Authors
- Abstract
- Subject/Category
- Publication Date

### Citations Text File
The `citations.txt` should contain citation data for calculating Pennant scores.

## Usage

### Basic Search
1. Enter your search query in the main search box
2. Use the personalization slider to balance between diversity (Pennant) and relevance (LDA)
3. Apply filters for authors, subjects, or topics as needed

### Visualization Analysis
1. After searching, view the interactive Pennant diagram
2. Hover over points to see paper details
3. Click on points for detailed paper information
4. Use sector analysis to understand paper relationships

### User Features
1. Register an account or login
2. Save interesting papers to your personal library
3. Add research notes to papers
4. View your saved papers from the user menu

## Scoring System

### Integrated Score (Tümleşik)
- **Color**: Gray background
- **Calculation**: Combines LDA topic relevance with Pennant access metrics
- **Purpose**: Overall paper relevance ranking

### LDA Score
- **Color**: Blue background
- **Calculation**: Topic modeling relevance score
- **Purpose**: Semantic similarity to search query

### Pennant Score
- **Color**: Orange background
- **Calculation**: Access ease based on citation patterns
- **Purpose**: Measure of paper accessibility and impact

## Configuration

### Debug Mode
Set `DEBUG_MODE = True` in `app.py` for development.

### Database
The application uses SQLite database (`search_app.db`) which is automatically created on first run.

### Topic Modeling
Adjust LDA parameters in the `optimal_topic_calculator.py` file for your specific dataset.

## File Structure

```
KIDR_app/
├── app.py                 # Main Flask application
├── optimal_topic_calculator.py  # LDA topic optimization
├── run_app.sh            # Startup script
├── data/
│   ├── metadata.xlsx     # Paper metadata
│   └── citations.txt     # Citation data
├── static/
│   └── logo.png         # Application logo
├── templates/
│   ├── index.html       # Main interface
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   └── saved_papers.html # User library
└── search_app.db        # SQLite database
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built for academic research and literature discovery
- Utilizes advanced topic modeling and citation analysis
- Inspired by information retrieval and knowledge discovery principles

## Support

For questions or support, please open an issue on GitHub or contact me at mugeakbulut@gmail.com.
