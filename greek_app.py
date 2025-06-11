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
    st.header("Greek Vocabulary Flashcards")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Display current word
        current_word = GREEK_WORDS[st.session_state.current_word_index]
        
        # Card container
        with st.container():
            st.markdown("""
            <div style='text-align: center; padding: 20px; border: 2px solid #ddd; border-radius: 10px; margin: 20px 0;'>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<h2 style='color: #1f4e79;'>{current_word['greek']}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-style: italic; color: #666;'>/{current_word['pronunciation']}/</p>", unsafe_allow_html=True)
            
            if st.session_state.show_answer:
                st.markdown(f"<h3 style='color: #2d5a2d;'>{current_word['english']}</h3>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Control buttons
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("Show Answer" if not st.session_state.show_answer else "Hide Answer"):
                st.session_state.show_answer = not st.session_state.show_answer
                st.rerun()
        
        with col_b:
            if st.button("✅ Correct"):
                if st.session_state.show_answer:
                    st.session_state.score['correct'] += 1
                    st.session_state.score['total'] += 1
                    st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(GREEK_WORDS)
                    st.session_state.show_answer = False
                    st.rerun()
        
        with col_c:
            if st.button("❌ Incorrect"):
                if st.session_state.show_answer:
                    st.session_state.score['total'] += 1
                    st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(GREEK_WORDS)
                    st.session_state.show_answer = False
                    st.rerun()
        
        # Navigation
        col_prev, col_shuffle, col_next = st.columns(3)
        
        with col_prev:
            if st.button("⬅️ Previous"):
                st.session_state.current_word_index = (st.session_state.current_word_index - 1) % len(GREEK_WORDS)
                st.session_state.show_answer = False
                st.rerun()
        
        with col_shuffle:
            if st.button("Shuffle"):
                st.session_state.current_word_index = random.randint(0, len(GREEK_WORDS) - 1)
                st.session_state.show_answer = False
                st.rerun()
        
        with col_next:
            if st.button("➡️ Next"):
                st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(GREEK_WORDS)
                st.session_state.show_answer = False
                st.rerun()
        
        # Progress and score
        progress = (st.session_state.current_word_index + 1) / len(GREEK_WORDS)
        st.progress(progress)
        st.caption(f"Word {st.session_state.current_word_index + 1} of {len(GREEK_WORDS)}")
        
        if st.session_state.score['total'] > 0:
            accuracy = (st.session_state.score['correct'] / st.session_state.score['total']) * 100
            st.metric("Accuracy", f"{accuracy:.1f}%", f"{st.session_state.score['correct']}/{st.session_state.score['total']}")
        
        # Reset score button
        if st.button("Reset Score"):
            st.session_state.score = {'correct': 0, 'total': 0}
            st.rerun()

# Useful Phrases Tab
with tab2:
    st.header("Useful Greek Phrases")
    
    # Category selector
    categories = [phrase_group["category"] for phrase_group in USEFUL_PHRASES]
    selected_category = st.selectbox("Choose a category:", categories)
    
    # Find the selected category data
    selected_phrases = next(group["phrases"] for group in USEFUL_PHRASES if group["category"] == selected_category)
    
    # Display phrases
    for i, phrase in enumerate(selected_phrases):
        with st.container():
            st.markdown("""
            <div style='padding: 15px; border: 1px solid #ddd; border-radius: 8px; margin: 10px 0; background-color: #f9f9f9;'>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Greek:** {phrase['greek']}")
                st.markdown(f"**English:** {phrase['english']}")
                st.markdown(f"**Pronunciation:** /{phrase['pronunciation']}/")
            
            with col2:
                if st.button(f"🔊 Listen", key=f"listen_{selected_category}_{i}"):
                    st.info("Audio feature coming soon!")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Study tips
    st.subheader("Study Tips")
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