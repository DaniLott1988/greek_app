# Greek Language Learning App - "It's all Greek to Me"

**Project by:** Danielle Maria Perez Lott

## 1. Executive Summary

This project presents an interactive Greek language learning application built with Streamlit. The app provides two main learning modules: an Anki-style flashcard system for vocabulary acquisition and a comprehensive collection of useful phrases organized by practical categories. The application incorporates gamification elements through progress tracking and accuracy metrics to enhance the learning experience. All Greek content has been validated by native speakers to ensure linguistic accuracy and cultural appropriateness.

## 2. Objective

The application addresses the following learning goals:

- **Vocabulary Building:** How can spaced repetition and interactive flashcards improve retention of essential Greek vocabulary for beginners?

- **Practical Communication:** What are the most useful phrases organized by real-world scenarios (greetings, dining, directions, shopping) that enable basic communication in Greek?

- **Progress Tracking:** How can gamification elements motivate learners and provide clear feedback on their language acquisition progress?

## 3. Required Tools

**Core Framework:**
- Streamlit (web application framework)
- Python 3.7+ (programming language)

**Data Management:**
- Session state management for progress tracking
- Random module for shuffling functionality

**User Interface:**
- HTML/CSS styling for enhanced visual presentation
- Responsive design elements

## 4. Features

The application includes the following components:

**Word Anki Tab:**
- Interactive flashcard system with 20+ essential Greek words
- Show/hide answer functionality
- Correct/incorrect tracking with accuracy metrics
- Navigation controls (Previous, Next, Shuffle)
- Progress bar and score reset functionality

**Useful Phrases Tab:**
- Categorized phrase collections (Greetings, Dining, Directions, Shopping)
- Greek text with English translations and pronunciation guides
- Interactive category selection
- Study tips and cultural notes

**Additional Resources:**
- Sidebar with Greek alphabet introduction
- Grammar notes and cultural context
- Progress tracking dashboard

## 5. Installation and Usage

**Setup Instructions:**
1. Install required dependencies: `pip install streamlit`
2. Save the application code as `greek_app.py`
3. Run the application: `streamlit run greek_app.py`
4. Access the app in your browser at `http://localhost:8501`

**Usage Guidelines:**
- Start with the Word Anki tab for vocabulary building
- Use the Useful Phrases tab for practical communication scenarios
- Track your progress in the sidebar
- Practice pronunciation using the phonetic guides

## 6. Risks and Challenges

**Language Accuracy:** Ensuring grammatically correct and culturally appropriate Greek content requires native speaker validation. Solution: All phrases have been reviewed and corrected by individuals with extensive Greek language experience.

**User Engagement:** Maintaining learner motivation through repetitive vocabulary practice can be challenging. Solution: Gamification elements including scoring, progress tracking, and shuffle functionality enhance engagement.

**Pronunciation Guidance:** Without audio features, learners rely solely on phonetic transcriptions. Solution: Comprehensive pronunciation guides using standardized phonetic notation, with plans for future audio integration.

**Content Scalability:** Limited vocabulary and phrase collections may not meet diverse learning needs. Solution: Modular data structure allows for easy expansion of content across different proficiency levels.

## 7. Technical Architecture

**Session Management:** Utilizes Streamlit's session state to maintain user progress across interactions without requiring external databases.

**Data Structure:** Organized vocabulary and phrases in structured dictionaries for easy maintenance and expansion.

**Responsive Design:** Implements column layouts and container elements for optimal viewing across different screen sizes.

## 8. Future Enhancements

- Audio pronunciation features
- Expanded vocabulary categories
- Grammar exercises
- User authentication and progress persistence
- Mobile application development

## 9. Conclusion

The Greek Language Learning App successfully combines traditional flashcard methodology with modern web technology to create an engaging and effective language learning tool. With validated content from native speakers and intuitive user interface design, the application provides a solid foundation for Greek language acquisition. The modular architecture enables future expansion while maintaining simplicity for beginning learners.