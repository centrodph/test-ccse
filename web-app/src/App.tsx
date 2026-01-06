import { useState, useMemo } from 'react';
import './App.css';
import questionsData from './data/questions.json';
import QuestionCard from './components/QuestionCard';

// Define the type for our question data based on the JSON structure
interface Question {
  id: string;
  filename: string;
  question: string;
  anwser: string;
  questionText?: string; // Derived processed question text
}

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  
  // Filter questions based on search
  const filteredQuestions = useMemo(() => {
    return (questionsData as Question[]).filter(q => 
      q.question.toLowerCase().includes(searchTerm.toLowerCase()) || 
      q.id.includes(searchTerm)
    );
  }, [searchTerm]);

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="container header-content">
          <div className="logo-area">
            <span className="flag-icon">🇪🇸</span>
            <h1>Test de Nacionalidad Española</h1>
          </div>
          <div className="search-bar">
            <input 
              type="text" 
              placeholder="Buscar pregunta..." 
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <span className="search-icon">🔍</span>
          </div>
        </div>
      </header>

      <main className="container main-content">
        <div className="stats-bar">
          <p>Mostrando <strong>{filteredQuestions.length}</strong> de <strong>{questionsData.length}</strong> preguntas</p>
        </div>
        
        <div className="questions-grid">
          {filteredQuestions.map((q) => (
            <QuestionCard key={q.id} question={q} />
          ))}
          
          {filteredQuestions.length === 0 && (
            <div className="no-results">
              <p>No se encontraron preguntas que coincidan con tu búsqueda.</p>
            </div>
          )}
        </div>
      </main>

      <footer className="app-footer">
        <div className="container">
          <p>© {new Date().getFullYear()} Estudio de Nacionalidad. Buena suerte! 🍀</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
