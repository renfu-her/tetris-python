"""
Ranking system for both single-player and two-player modes
Handles high scores and live ranking display
"""

import json
import os


class RankingSystem:
    """Manages rankings and high scores"""
    
    def __init__(self, filename='high_scores.json'):
        self.filename = filename
        self.high_scores = []
        self.load_high_scores()
    
    def load_high_scores(self):
        """Load high scores from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.high_scores = json.load(f)
            except:
                self.high_scores = []
        else:
            self.high_scores = []
        
        # Sort by score descending
        self.high_scores.sort(key=lambda x: x['score'], reverse=True)
        # Keep only top 10
        self.high_scores = self.high_scores[:10]
    
    def save_high_scores(self):
        """Save high scores to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.high_scores, f, indent=2)
        except:
            pass
    
    def add_score(self, score, level, lines_cleared):
        """Add a new high score"""
        entry = {
            'score': score,
            'level': level,
            'lines': lines_cleared
        }
        
        self.high_scores.append(entry)
        self.high_scores.sort(key=lambda x: x['score'], reverse=True)
        self.high_scores = self.high_scores[:10]
        self.save_high_scores()
    
    def is_high_score(self, score):
        """Check if score qualifies as high score"""
        if len(self.high_scores) < 10:
            return True
        return score > self.high_scores[-1]['score']
    
    def get_rank(self, score):
        """Get rank of a score (1-based)"""
        rank = 1
        for entry in self.high_scores:
            if score > entry['score']:
                return rank
            rank += 1
        return rank if len(self.high_scores) < 10 else None
    
    def get_top_scores(self, limit=10):
        """Get top N high scores"""
        return self.high_scores[:limit]

