import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="It's All Greek To Me",
    page_icon="🇬🇷",
    layout="wide"
)

# Initialize session state
if 'current_word_index' not in st.session_state:
    st.session_state.current_word_index = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'score' not in st.session_state:
    st.session_state.score = {'correct': 0, 'total': 0}

# Greek vocabulary data
GREEK_WORDS = [
    {"greek": "γεια σας", "english": "hello (formal)", "pronunciation": "yah-sas"},
    {"greek": "γεια σου", "english": "hello (informal)", "pronunciation": "yah-soo"},
    {"greek": "αντίο", "english": "goodbye", "pronunciation": "ah-DEE-oh"},
    {"greek": "παρακαλώ", "english": "please/you're welcome", "pronunciation": "pah-rah-kah-LOH"},
    {"greek": "ευχαριστώ", "english": "thank you", "pronunciation": "ef-khah-ree-STOH"},
    {"greek": "συγγνώμη", "english": "excuse me/sorry", "pronunciation": "see-GHNOH-mee"},
    {"greek": "ναι", "english": "yes", "pronunciation": "neh"},
    {"greek": "όχι", "english": "no", "pronunciation": "OH-khee"},
    {"greek": "νερό", "english": "water", "pronunciation": "neh-ROH"},
    {"greek": "φαγητό", "english": "food", "pronunciation": "fah-ghee-TOH"},
    {"greek": "σπίτι", "english": "house", "pronunciation": "SPEE-tee"},
    {"greek": "δρόμος", "english": "road/street", "pronunciation": "DROH-mos"},
    {"greek": "καλημέρα", "english": "good morning", "pronunciation": "kah-lee-MEH-rah"},
    {"greek": "καλησπέρα", "english": "good evening", "pronunciation": "kah-lee-SPEH-rah"},
    {"greek": "καληνύχτα", "english": "good night", "pronunciation": "kah-lee-NIKH-tah"},
    {"greek": "πόσο κάνει", "english": "how much does it cost", "pronunciation": "POH-so KAH-nee"},
    {"greek": "δεν καταλαβαίνω", "english": "I don't understand", "pronunciation": "dhen kah-tah-lah-VEH-no"},
    {"greek": "μιλάτε αγγλικά", "english": "do you speak English", "pronunciation": "mee-LAH-teh ah-glee-KAH"},
    {"greek": "με λένε", "english": "my name is", "pronunciation": "meh LEH-neh"},
    {"greek": "τι κάνετε", "english": "how are you (formal)", "pronunciation": "tee KAH-neh-teh"}
]

# Useful phrases data
USEFUL_PHRASES = [
    {
        "category": "Greetings",
        "phrases": [
            {"greek": "Καλημέρα! Πώς είστε;", "english": "Good morning! How are you?", "pronunciation": "kah-lee-MEH-rah! pos EE-steh?"},
            {"greek": "Χαίρομαι που σας γνωρίζω", "english": "Nice to meet you", "pronunciation": "KHEH-ro-meh poo sas gno-REE-zo"},
            {"greek": "Τι κάνεις;", "english": "How are you? (informal)", "pronunciation": "tee KAH-nees?"}
        ]
    },
    {
        "category": "Dining",
        "phrases": [
            {"greek": "Θα θέλαμε το μενού, παρακαλώ", "english": "We would like the menu, please", "pronunciation": "thah THEH-lah-meh to meh-NOO, pah-rah-kah-LOH"},
            {"greek": "Τι προτείνετε;", "english": "What do you recommend?", "pronunciation": "tee pro-TEE-neh-teh?"},
            {"greek": "Τον λογαριασμό, παρακαλώ", "english": "The bill, please", "pronunciation": "ton lo-ghah-ree-ahs-MOH, pah-rah-kah-LOH"}
        ]
    },
    {
        "category": "Directions",
        "phrases": [
            {"greek": "Πού είναι το ξενοδοχείο;", "english": "Where is the hotel?", "pronunciation": "poo EE-neh to kseh-no-dho-KHEE-o?"},
            {"greek": "Μπορείτε να με βοηθήσετε;", "english": "Can you help me?", "pronunciation": "bo-REE-teh nah meh vo-ee-THEE-seh-teh?"},
            {"greek": "Δεν ξέρω που είμαι", "english": "I don't know where I am / I'm lost", "pronunciation": "dhen KSEH-ro poo EE-meh"}
        ]
    },
    {
        "category": "Shopping",
        "phrases": [
            {"greek": "Πόσο κοστίζει αυτό;", "english": "How much does this cost?", "pronunciation": "POH-so ko-STEE-zee af-TOH?"},
            {"greek": "Μπορώ να το δοκιμάσω;", "english": "Can I try it on?", "pronunciation": "bo-ROH nah to dho-kee-MAH-so?"},
            {"greek": "Έχετε αυτό σε άλλο μέγεθος;", "english": "Do you have this in another size?", "pronunciation": "EH-kheh-teh af-TOH seh AH-lo MEH-gheh-thos?"}
        ]
    }
]

# App title and description
st.title("🇬🇷 It's All Greek To Me")
st.markdown("Learn Greek vocabulary and useful phrases interactively!")

# Create tabs
tab1, tab2 = st.tabs(["Word Anki", "Useful Phrases"])

# Word Anki Tab
with tab1:
    # Center content on desktop using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h2 style='text-align: center; margin: 0;'>Greek Vocabulary Flashcards</h2>", unsafe_allow_html=True)
        
        # Display current word
        current_word = GREEK_WORDS[st.session_state.current_word_index]
        
        # Card container - centered and mobile-friendly with theme adaptation
        with st.container():
            st.markdown(f"<div style='text-align: center;'><h2>{current_word['greek']}</h2></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center;'><em>/{current_word['pronunciation']}/</em></div>", unsafe_allow_html=True)
            
            if st.session_state.show_answer:
                st.markdown(f"<div style='text-align: center;'><h3>{current_word['english']}</h3></div>", unsafe_allow_html=True)
            
            st.markdown("---")
        
        # Control buttons - full width for mobile
        if st.button("Show Answer" if not st.session_state.show_answer else "Hide Answer", 
                     use_container_width=True, type="primary"):
            st.session_state.show_answer = not st.session_state.show_answer
            st.rerun()
        
        # Rating buttons - only show when answer is visible
        if st.session_state.show_answer:
            col_correct, col_incorrect = st.columns(2)
            
            with col_correct:
                if st.button("✅ Correct", use_container_width=True, type="secondary"):
                    st.session_state.score['correct'] += 1
                    st.session_state.score['total'] += 1
                    st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(GREEK_WORDS)
                    st.session_state.show_answer = False
                    st.rerun()
            
            with col_incorrect:
                if st.button("❌ Incorrect", use_container_width=True):
                    st.session_state.score['total'] += 1
                    st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(GREEK_WORDS)
                    st.session_state.show_answer = False
                    st.rerun()
        
        st.divider()
        
        # Navigation buttons
        col_prev, col_shuffle, col_next = st.columns(3)
        
        with col_prev:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_word_index = (st.session_state.current_word_index - 1) % len(GREEK_WORDS)
                st.session_state.show_answer = False
                st.rerun()
        
        with col_shuffle:
            if st.button("Shuffle", use_container_width=True):
                st.session_state.current_word_index = random.randint(0, len(GREEK_WORDS) - 1)
                st.session_state.show_answer = False
                st.rerun()
        
        with col_next:
            if st.button("➡️ Next", use_container_width=True):
                st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(GREEK_WORDS)
                st.session_state.show_answer = False
                st.rerun()
        
        # Progress and score
        progress = (st.session_state.current_word_index + 1) / len(GREEK_WORDS)
        st.progress(progress)
        st.caption(f"Word {st.session_state.current_word_index + 1} of {len(GREEK_WORDS)}")
        
        if st.session_state.score['total'] > 0:
            accuracy = (st.session_state.score['correct'] / st.session_state.score['total']) * 100
            col_acc, col_reset = st.columns([2, 1])
            with col_acc:
                st.metric("Accuracy", f"{accuracy:.1f}%", f"{st.session_state.score['correct']}/{st.session_state.score['total']}")
            with col_reset:
                if st.button("🔄 Reset", use_container_width=True):
                    st.session_state.score = {'correct': 0, 'total': 0}
                    st.rerun()

# Useful Phrases Tab
with tab2:
    # Center content on desktop using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h2 style='text-align: center; margin: 0;'>Useful Greek Phrases</h2>", unsafe_allow_html=True)
        
        # Category selector
        categories = [phrase_group["category"] for phrase_group in USEFUL_PHRASES]
        selected_category = st.selectbox("Choose a category:", categories)
        
        # Find the selected category data
        selected_phrases = next(group["phrases"] for group in USEFUL_PHRASES if group["category"] == selected_category)
        
        # Display phrases - mobile-friendly cards with theme adaptation
        for i, phrase in enumerate(selected_phrases):
            with st.container():
                st.markdown(f"**Greek:** {phrase['greek']}")
                st.markdown(f"**English:** {phrase['english']}")
                st.markdown(f"**Pronunciation:** /{phrase['pronunciation']}/")
                
                st.divider()
        
        # Study tips
        st.markdown("<h3 style='text-align: center; margin: 0;'>Study Tips</h3>", unsafe_allow_html=True)
        with st.expander("Click to see study tips"):
            tips = [
                "Practice pronunciation by reading the phonetic transcriptions out loud",
                "Try to use these phrases in real conversations",
                "Focus on one category at a time to avoid overwhelming yourself",
                "Greek has different forms for masculine and feminine - pay attention to context",
                "The Greek alphabet has 24 letters - consider learning it to read Greek text better"
            ]
            
            for tip in tips:
                st.markdown(f"• {tip}")

# Sidebar with additional information
with st.sidebar:
    st.header("Learning Resources")
    st.markdown("""
    **Greek Alphabet:**
    - Α α (Alpha)
    - Β β (Beta) 
    - Γ γ (Gamma)
    - Δ δ (Delta)
    - And 20 more letters...
    
    **Quick Grammar Notes:**
    - Greek has 3 genders: masculine, feminine, neuter
    - Verbs change endings based on person and tense
    - Adjectives must agree with nouns in gender, number, and case
    
    **Cultural Notes:**
    - Greeks often gesture while speaking
    - Hospitality (φιλοξενία) is very important in Greek culture
    - Many English words come from Greek roots
    """)
    
    st.header("Your Progress")
    if st.session_state.score['total'] > 0:
        st.metric("Words Studied", st.session_state.score['total'])
        st.metric("Correct Answers", st.session_state.score['correct'])
    else:
        st.info("Start practicing to see your progress!")