import { useState, useRef, useEffect } from 'react';
import './QuestionCard.css';

interface QuestionProps {
  question: {
    id: string;
    filename: string;
    question: string;
    anwser: string;
  };
}

const QuestionCard = ({ question }: QuestionProps) => {
  const [isRevealed, setIsRevealed] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  // Audio path relative to public folder
  const audioSrc = `audios/${question.filename}`;

  const toggleReveal = () => {
    setIsRevealed(!isRevealed);
  };

  const toggleAudio = (e: React.MouseEvent) => {
    e.stopPropagation(); // Prevent card click if we click audio button
    
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };
  
  // Handle audio ending
  const onAudioEnded = () => {
    setIsPlaying(false);
  };

  // Reset state when question changes
  useEffect(() => {
    setIsRevealed(false);
    setIsPlaying(false);
    if(audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
  }, [question.id]);

  return (
    <div className={`question-card ${isRevealed ? 'revealed' : ''}`}>
      <div className="card-header">
        <span className="question-id">#{question.id}</span>
        <button 
          className={`audio-btn ${isPlaying ? 'playing' : ''}`}
          onClick={toggleAudio}
          title={isPlaying ? "Pausar audio" : "Escuchar audio"}
        >
          {isPlaying ? (
            <span className="icon-pause">⏸</span>
          ) : (
            <span className="icon-play">▶️</span>
          )}
        </button>
        <audio 
          ref={audioRef} 
          src={audioSrc} 
          onEnded={onAudioEnded}
          onPause={() => setIsPlaying(false)}
          onPlay={() => setIsPlaying(true)}
        />
      </div>
      
      <div className="card-content">
        <h3 className="question-text">{question.question}</h3>
      </div>
      
      <div className="card-footer">
        {isRevealed ? (
          <div className="answer-box">
             <p className="answer-label">Respuesta Correcta:</p>
             <p className="answer-text">{question.anwser}</p>
          </div>
        ) : (
          <button className="reveal-btn" onClick={toggleReveal}>
            Ver Respuesta
          </button>
        )}
      </div>
    </div>
  );
};

export default QuestionCard;
