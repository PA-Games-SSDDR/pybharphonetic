def hindi_to_assamese(input_text):
    # Mapping dictionary for Hindi to Assamese characters
    hindi_to_assamese_mapping = {
        'अ': 'অ', 'आ': 'আ', 'इ': 'ই', 'ई': 'ঈ', 'उ': 'উ', 'ऊ': 'ঊ',
        'ऋ': 'ঋ', 'ए': 'এ', 'ऐ': 'ঐ', 'ओ': 'ও', 'औ': 'ঔ',
        'क': 'ক', 'ख': 'খ', 'ग': 'গ', 'घ': 'ঘ', 'ङ': 'ঙ',
        'च': 'চ', 'छ': 'ছ', 'ज': 'জ', 'झ': 'ঝ', 'ञ': 'ঞ',
        'ट': 'ট', 'ठ': 'ঠ', 'ड': 'ড', 'ढ': 'ঢ', 'ण': 'ণ',
        'त': 'ত', 'थ': 'থ', 'द': 'দ', 'ध': 'ধ', 'न': 'ন',
        'प': 'প', 'फ': 'ফ', 'ब': 'ব', 'भ': 'ভ', 'म': 'ম',
        'य': 'য', 'र': 'ৰ', 'ल': 'ল', 'व': 'ৱ', 'श': 'শ',
        'ष': 'ষ', 'स': 'স', 'ह': 'হ',
        '०': '০', '१': '১', '२': '২', '३': '৩', '४': '৪',
        '५': '৫', '६': '৬', '७': '৭', '८': '৮', '९': '৯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Assamese using the mapping dictionary
    output_text = ''.join(hindi_to_assamese_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_bodo(input_text):
    # Mapping dictionary for Hindi to Bodo characters
    hindi_to_bodo_mapping = {
        'अ': 'ꞵ', 'आ': 'Ꭓ', 'इ': 'Ꞷ', 'ई': 'ꞷ', 'उ': 'Ꞹ', 'ऊ': 'ꞹ',
        'ऋ': 'ꞻ', 'ए': 'ꞽ', 'ऐ': 'Ꞿ', 'ओ': 'Ꟃ', 'औ': 'ꟃ',
        'क': 'Ʞ', 'ख': 'Ʇ', 'ग': 'Ʝ', 'घ': 'Ꭓ', 'ङ': 'Ꞵ',
        'च': 'ꞵ', 'छ': 'Ꞷ', 'ज': 'ꞷ', 'झ': 'Ꞹ', 'ञ': 'ꞹ',
        'ट': 'Ꞻ', 'ठ': 'ꞻ', 'ड': 'Ꞽ', 'ढ': 'ꞽ', 'ण': 'Ꞿ',
        'त': 'ꞿ', 'थ': 'Ꟁ', 'द': 'ꟁ', 'ध': 'Ꟃ', 'न': 'ꟃ',
        'प': 'Ꞔ', 'फ': 'Ʂ', 'ब': 'Ᶎ', 'भ': 'Ꟈ', 'म': 'ꟈ',
        'य': 'Ꟊ', 'र': 'ꟊ', 'ल': 'Ɤ', 'व': 'Ꟍ', 'श': 'ꟍ',
        'ष': '꟎', 'स': '꟏', 'ह': 'Ꟑ',
        '०': '০', '१': '১', '२': '২', '३': '৩', '४': '৪',
        '५': '৫', '६': '৬', '७': '৭', '८': '৮', '९': '৯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Bodo using the mapping dictionary
    output_text = ''.join(hindi_to_bodo_mapping.get(char, char) for char in input_text)
    return output_text


def hindi_to_dogri(input_text):
    # Mapping dictionary for Hindi to Dogri characters
    hindi_to_dogri_mapping = {
        'अ': 'ਅ', 'आ': 'ਆ', 'इ': 'ਇ', 'ई': 'ਈ', 'उ': 'ਉ', 'ऊ': 'ਊ',
        'ऋ': '਋', 'ए': 'ਏ', 'ऐ': 'ਐ', 'ओ': 'ਓ', 'औ': 'ਔ',
        'क': 'ਕ', 'ख': 'ਖ', 'ग': 'ਗ', 'घ': 'ਘ', 'ङ': 'ਙ',
        'च': 'ਚ', 'छ': 'ਛ', 'ज': 'ਜ', 'झ': 'ਝ', 'ञ': 'ਞ',
        'ट': 'ਟ', 'ठ': 'ਠ', 'ड': 'ਡ', 'ढ': 'ਢ', 'ण': 'ਣ',
        'त': 'ਤ', 'थ': 'ਥ', 'द': 'ਦ', 'ध': 'ਧ', 'न': 'ਨ',
        'प': 'ਪ', 'फ': 'ਫ', 'ब': 'ਬ', 'भ': 'ਭ', 'म': 'ਮ',
        'य': 'ਯ', 'र': 'ਰ', 'ल': 'ਲ', 'व': 'ਵ', 'श': 'ਸ਼',
        'ष': '਷', 'स': 'ਸ', 'ह': 'ਹ',
        '०': '੦', '१': '੧', '२': '੨', '३': '੩', '४': '੪',
        '५': '੫', '६': '੬', '७': '੭', '८': '੮', '९': '੯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Dogri using the mapping dictionary
    output_text = ''.join(hindi_to_dogri_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_gujarati(input_text):
    # Mapping dictionary for Hindi to Gujarati characters
    hindi_to_gujarati_mapping = {
        'अ': 'અ', 'आ': 'આ', 'इ': 'ઇ', 'ई': 'ઈ', 'उ': 'ઉ', 'ऊ': 'ઊ',
        'ऋ': 'ઋ', 'ए': 'એ', 'ऐ': 'ઐ', 'ओ': 'ઓ', 'औ': 'ઔ',
        'क': 'ક', 'ख': 'ખ', 'ग': 'ગ', 'घ': 'ઘ', 'ङ': 'ઙ',
        'च': 'ચ', 'छ': 'છ', 'ज': 'જ', 'झ': 'ઝ', 'ञ': 'ઞ',
        'ट': 'ટ', 'ठ': 'ઠ', 'ड': 'ડ', 'ढ': 'ઢ', 'ण': 'ણ',
        'त': 'ત', 'थ': 'થ', 'द': 'દ', 'ध': 'ધ', 'न': 'ન',
        'प': 'પ', 'फ': 'ફ', 'ब': 'બ', 'भ': 'ભ', 'म': 'મ',
        'य': 'ય', 'र': 'ર', 'ल': 'લ', 'व': 'વ', 'श': 'શ',
        'ष': 'ષ', 'स': 'સ', 'ह': 'હ',
        '०': '૦', '१': '૧', '२': '૨', '३': '૩', '४': '૪',
        '५': '૫', '६': '૬', '७': '૭', '८': '૮', '९': '૯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Gujarati using the mapping dictionary
    output_text = ''.join(hindi_to_gujarati_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_kannada(input_text):
    # Mapping dictionary for Hindi to Kannada characters
    hindi_to_kannada_mapping = {
        'अ': 'ಅ', 'आ': 'ಆ', 'इ': 'ಇ', 'ई': 'ಈ', 'उ': 'ಉ', 'ऊ': 'ಊ',
        'ऋ': 'ಋ', 'ए': 'ಎ', 'ऐ': 'ಐ', 'ओ': 'ಒ', 'औ': 'ಔ',
        'क': 'ಕ', 'ख': 'ಖ', 'ग': 'ಗ', 'घ': 'ಘ', 'ङ': 'ಙ',
        'च': 'ಚ', 'छ': 'ಛ', 'ज': 'ಜ', 'झ': 'ಝ', 'ञ': 'ಞ',
        'ट': 'ಟ', 'ठ': 'ಠ', 'ड': 'ಡ', 'ढ': 'ಢ', 'ण': 'ಣ',
        'त': 'ತ', 'थ': 'ಥ', 'द': 'ದ', 'ध': 'ಧ', 'न': 'ನ',
        'प': 'ಪ', 'फ': 'ಫ', 'ब': 'ಬ', 'भ': 'ಭ', 'म': 'ಮ',
        'य': 'ಯ', 'र': 'ರ', 'ल': 'ಲ', 'व': 'ವ', 'श': 'ಶ',
        'ष': 'ಷ', 'स': 'ಸ', 'ह': 'ಹ',
        '०': '೦', '१': '೧', '२': '೨', '३': '೩', '४': '೪',
        '५': '೫', '६': '೬', '७': '೭', '८': '೮', '९': '೯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Kannada using the mapping dictionary
    output_text = ''.join(hindi_to_kannada_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_kashmiri(input_text):
    # Mapping dictionary for Hindi to Kashmiri characters
    hindi_to_kashmiri_mapping = {
        'अ': 'ا', 'आ': 'آ', 'इ': 'ہ', 'ई': 'ہٚ', 'उ': 'وٗ', 'ऊ': 'وٗٚ',
        'ऋ': 'رِ', 'ए': 'ے', 'ऐ': 'ئے', 'ओ': 'وہ', 'औ': 'ؤہ',
        'क': 'ک', 'ख': 'خ', 'ग': 'گ', 'घ': 'غ', 'ङ': 'نٛ',
        'च': 'چ', 'छ': 'ژ', 'ज': 'ج', 'झ': 'ز', 'ञ': 'نٛ',
        'ट': 'ٹ', 'ठ': 'ٹھ', 'ड': 'ڈ', 'ढ': 'ڈھ', 'ण': 'ں',
        'त': 'ت', 'थ': 'تھ', 'द': 'د', 'ध': 'ذ', 'न': 'ن',
        'प': 'پ', 'फ': 'ف', 'ब': 'ب', 'भ': 'بھ', 'म': 'م',
        'य': 'ے', 'र': 'ر', 'ल': 'ل', 'व': 'و', 'श': 'ش',
        'ष': 'ښ', 'स': 'س', 'ह': 'ہ',
        '०': '۰', '१': '۱', '२': '۲', '३': '۳', '४': '۴',
        '५': '۵', '६': '۶', '७': '۷', '८': '۸', '९': '۹',
        '","': '،', '.': '۔', '?': '؟', '!': '!', ':': ':', ';': '؛',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Kashmiri using the mapping dictionary
    output_text = ''.join(hindi_to_kashmiri_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_malayalam(input_text):
    # Mapping dictionary for Hindi to Malayalam characters
    hindi_to_malayalam_mapping = {
        'अ': 'അ', 'आ': 'ആ', 'इ': 'ഇ', 'ई': 'ഈ', 'उ': 'ഉ', 'ऊ': 'ഊ',
        'ऋ': 'ഋ', 'ए': 'എ', 'ऐ': 'ഐ', 'ओ': 'ഓ', 'औ': 'ഔ',
        'क': 'ക', 'ख': 'ഖ', 'ग': 'ഗ', 'घ': 'ഘ', 'ङ': 'ങ',
        'च': 'ച', 'छ': 'ഛ', 'ज': 'ജ', 'झ': 'ഝ', 'ञ': 'ഞ',
        'ट': 'ട', 'ठ': 'ഠ', 'ड': 'ഡ', 'ढ': 'ഢ', 'ण': 'ണ',
        'त': 'ത', 'थ': 'ഥ', 'द': 'ദ', 'ध': 'ധ', 'न': 'ന',
        'प': 'പ', 'फ': 'ഫ', 'ब': 'ബ', 'भ': 'ഭ', 'म': 'മ',
        'य': 'യ', 'र': 'ര', 'ल': 'ല', 'व': 'വ', 'श': 'ശ',
        'ष': 'ഷ', 'स': 'സ', 'ह': 'ഹ',
        '०': '൦', '१': '൧', '२': '൨', '३': '൩', '४': '൪',
        '५': '൫', '६': '൬', '७': '൭', '८': '൮', '९': '൯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Malayalam using the mapping dictionary
    output_text = ''.join(hindi_to_malayalam_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_manipuri(input_text):
    # Mapping dictionary for Hindi to Manipuri characters
    hindi_to_manipuri_mapping = {
        'अ': 'ꯃ', 'आ': 'ꯄ', 'इ': 'ꯅ', 'ई': 'ꯆ', 'उ': 'ꯇ', 'ऊ': 'ꯈ',
        'ऋ': 'ꯉ', 'ए': 'ꯋ', 'ऐ': 'ꯌ', 'ओ': 'ꯍ', 'औ': 'ꯎ',
        'क': 'ꯐ', 'ख': 'ꯑ', 'ग': 'ꯒ', 'घ': 'ꯓ', 'ङ': 'ꯔ',
        'च': 'ꯕ', 'छ': 'ꯖ', 'ज': 'ꯗ', 'झ': 'ꯘ', 'ञ': 'ꯙ',
        'ट': 'ꯚ', 'ठ': 'ꯛ', 'ड': 'ꯜ', 'ढ': 'ꯝ', 'ण': 'ꯞ',
        'त': 'ꯟ', 'थ': 'ꯠ', 'द': 'ꯡ', 'ध': 'ꯢ', 'न': 'ꯣ',
        'प': 'ꯤ', 'फ': 'ꯥ', 'ब': 'ꯦ', 'भ': 'ꯧ', 'म': 'ꯨ',
        'य': 'ꯩ', 'र': 'ꯪ', 'ल': '꯫', 'व': '꯬', 'श': '꯭',
        'ष': '꯮', 'स': '꯯', 'ह': '꯰',
        '०': '০', '१': '১', '२': '২', '३': '৩', '४': '৪',
        '५': '৫', '६': '৬', '७': '৭', '८': '৮', '९': '৯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Manipuri using the mapping dictionary
    output_text = ''.join(hindi_to_manipuri_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_odia(input_text):
    # Mapping dictionary for Hindi to Odia characters
    hindi_to_odia_mapping = {
        'अ': 'ଅ', 'आ': 'ଆ', 'इ': 'ଇ', 'ई': 'ଈ', 'उ': 'ଉ', 'ऊ': 'ଊ',
        'ऋ': 'ଋ', 'ए': 'ଏ', 'ऐ': 'ଐ', 'ओ': 'ଓ', 'औ': 'ଔ',
        'क': 'କ', 'ख': 'ଖ', 'ग': 'ଗ', 'घ': 'ଘ', 'ङ': 'ଙ',
        'च': 'ଚ', 'छ': 'ଛ', 'ज': 'ଜ', 'झ': 'ଝ', 'ञ': 'ଞ',
        'ट': 'ଟ', 'ठ': 'ଠ', 'ड': 'ଡ', 'ढ': 'ଢ', 'ण': 'ଣ',
        'त': 'ତ', 'थ': 'ଥ', 'द': 'ଦ', 'ध': 'ଧ', 'न': 'ନ',
        'प': 'ପ', 'फ': 'ଫ', 'ब': 'ବ', 'भ': 'ଭ', 'म': 'ମ',
        'य': 'ଯ', 'र': 'ର', 'ल': 'ଲ', 'व': 'ଵ', 'श': 'ଶ',
        'ष': 'ଷ', 'स': 'ସ', 'ह': 'ହ',
        '०': '୦', '१': '୧', '२': '୨', '३': '୩', '४': '୪',
        '५': '୫', '६': '୬', '७': '୭', '८': '୮', '९': '୯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Odia using the mapping dictionary
    output_text = ''.join(hindi_to_odia_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_punjabi(input_text):
    # Mapping dictionary for Hindi to Punjabi characters
    hindi_to_punjabi_mapping = {
        'अ': 'ਅ', 'आ': 'ਆ', 'इ': 'ਇ', 'ई': 'ਈ', 'उ': 'ਉ', 'ऊ': 'ਊ',
        'ऋ': '਋', 'ए': 'ਏ', 'ऐ': 'ਐ', 'ओ': 'ਓ', 'औ': 'ਔ',
        'क': 'ਕ', 'ख': 'ਖ', 'ग': 'ਗ', 'घ': 'ਘ', 'ङ': 'ਙ',
        'च': 'ਚ', 'छ': 'ਛ', 'ज': 'ਜ', 'झ': 'ਝ', 'ञ': 'ਞ',
        'ट': 'ਟ', 'ठ': 'ਠ', 'ड': 'ਡ', 'ढ': 'ਢ', 'ण': 'ਣ',
        'त': 'ਤ', 'थ': 'ਥ', 'द': 'ਦ', 'ध': 'ਧ', 'न': 'ਨ',
        'प': 'ਪ', 'फ': 'ਫ', 'ब': 'ਬ', 'भ': 'ਭ', 'म': 'ਮ',
        'य': 'ਯ', 'र': 'ਰ', 'ल': 'ਲ', 'व': 'ਵ', 'श': 'ਸ਼',
        'ष': '਷', 'स': 'ਸ', 'ह': 'ਹ',
        '०': '੦', '१': '੧', '२': '੨', '३': '੩', '४': '੪',
        '५': '੫', '६': '੬', '७': '੭', '८': '੮', '९': '੯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Punjabi using the mapping dictionary
    output_text = ''.join(hindi_to_punjabi_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_santhali(input_text):
    # Basic mapping from Hindi Devanagari characters to Santhali Ol Chiki script
    hindi_to_santhali_mapping = {
        'अ': 'ᱟ', 'आ': 'ᱟᱪ', 'इ': 'ᱞ', 'ई': 'ᱞᱪ', 'उ': 'ᱮ', 'ऊ': 'ᱮᱪ',
        'ऋ': 'ᱞᱟ', 'ए': 'ᱞᱤ', 'ऐ': 'ᱞᱤᱪ', 'ओ': 'ᱮᱤ', 'औ': 'ᱮᱤᱪ',
        'क': 'ᱠ', 'ख': 'ᱠᱚ', 'ग': 'ᱢ', 'घ': 'ᱢᱚ', 'ङ': 'ᱡ',
        'च': 'ᱪ', 'छ': 'ᱪᱚ', 'ज': 'ᱤ', 'झ': 'ᱤᱚ', 'ञ': 'ᱤᱟ',
        'ट': 'ᱴ', 'ठ': 'ᱴᱚ', 'ड': 'ᱢ', 'ढ': 'ᱢᱚ', 'ण': 'ᱦ',
        'त': 'ᱩ', 'थ': 'ᱩᱚ', 'द': 'ᱦ', 'ध': 'ᱦᱚ', 'न': 'ᱧ',
        'प': 'ᱯ', 'फ': 'ᱯᱚ', 'ब': 'ᱰ', 'भ': 'ᱰᱚ', 'म': 'ᱮ',
        'य': 'ᱨ', 'र': 'ᱨ', 'ल': 'ᱳ', 'व': 'ᱥ', 'श': 'ᱧ',
        'ष': 'ᱧ', 'स': 'ᱥ', 'ह': 'ᱦ',
        '०': '᱐', '१': '᱑', '२': '᱒', '३': '᱓', '४': '᱔',
        '५': '᱕', '६': '᱖', '७': '᱗', '८': '᱘', '९': '᱙',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Santhali using the mapping dictionary
    output_text = ''.join(hindi_to_santhali_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_sindhi(input_text):
    # Basic mapping from Hindi Devanagari characters to Sindhi script
    hindi_to_sindhi_mapping = {
        'अ': 'ا', 'आ': 'آ', 'इ': 'اِ', 'ई': 'اَ', 'उ': 'اُ', 'ऊ': 'وُ',
        'ऋ': 'ٻ', 'ए': 'اے', 'ऐ': 'ٺ', 'ओ': 'او', 'औ': 'اَو',
        'क': 'ڪ', 'ख': 'ڪھ', 'ग': 'گ', 'घ': 'گھ', 'ङ': 'ڱ',
        'च': 'چ', 'छ': 'ڇ', 'ज': 'ج', 'झ': 'ڄ', 'ञ': 'ݙ',
        'ट': 'ٹ', 'ठ': 'ٺ', 'ड': 'ڏ', 'ढ': 'ڌ', 'ण': 'ڻ',
        'त': 'ٽ', 'थ': 'ٿ', 'द': 'ڌ', 'ध': 'ڍ', 'न': 'ن',
        'प': 'پ', 'फ': 'ف', 'ब': 'ب', 'भ': 'ٻ', 'म': 'م',
        'य': 'ي', 'र': 'ر', 'ल': 'ل', 'व': 'و', 'श': 'ش',
        'ष': 'ݜ', 'स': 'س', 'ह': 'ه',
        '०': '٠', '१': '١', '२': '٢', '३': '٣', '४': '٤',
        '५': '٥', '६': '٦', '७': '٧', '८': '٨', '९': '٩',
        '","': '،', '.': '۔', '?': '؟', '!': '!', '":"': '۔', ';': '؛',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Sindhi using the mapping dictionary
    output_text = ''.join(hindi_to_sindhi_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_tamil(input_text):
    # Basic mapping from Hindi Devanagari characters to Tamil script
    hindi_to_tamil_mapping = {
        'अ': 'அ', 'आ': 'ஆ', 'इ': 'இ', 'ई': 'ஈ', 'उ': 'உ', 'ऊ': 'ஊ',
        'ऋ': '஋', 'ए': 'ஏ', 'ऐ': 'ஐ', 'ओ': 'ஓ', 'औ': 'ஔ',
        'क': 'க', 'ख': 'க', 'ग': 'க', 'घ': 'க', 'ङ': 'ங',
        'च': 'ச', 'छ': 'ச', 'ज': 'ஜ', 'झ': 'ஜ', 'ञ': 'ஞ',
        'ट': 'ட', 'ठ': 'ட', 'ड': 'ட', 'ढ': 'ட', 'ण': 'ண',
        'त': 'த', 'थ': 'த', 'द': 'த', 'ध': 'த', 'न': 'ந',
        'प': 'ப', 'फ': 'ப', 'ब': 'ப', 'भ': 'ப', 'म': 'ம',
        'य': 'ய', 'र': 'ர', 'ल': 'ல', 'व': 'வ', 'श': 'ச',
        'ष': 'ஷ', 'स': 'ச', 'ह': 'ஹ',
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
        '५': '5', '६': '6', '७': '7', '८': '8', '९': '9',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Tamil using the mapping dictionary
    output_text = ''.join(hindi_to_tamil_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_telegu(input_text):
    # Basic mapping from Hindi Devanagari characters to Telugu script
    hindi_to_telugu_mapping = {
        'अ': 'అ', 'आ': 'ఆ', 'इ': 'ఇ', 'ई': 'ఈ', 'उ': 'ఉ', 'ऊ': 'ఊ',
        'ऋ': 'ఋ', 'ए': 'ఏ', 'ऐ': 'ఐ', 'ओ': 'ఓ', 'औ': 'ఔ',
        'क': 'క', 'ख': 'ఖ', 'ग': 'గ', 'घ': 'ఘ', 'ङ': 'ఙ',
        'च': 'చ', 'छ': 'ఛ', 'ज': 'జ', 'झ': 'ఝ', 'ञ': 'ఞ',
        'ट': 'ట', 'ठ': 'ఠ', 'ड': 'డ', 'ढ': 'ఢ', 'ण': 'ణ',
        'त': 'త', 'थ': 'థ', 'द': 'ద', 'ध': 'ధ', 'न': 'న',
        'प': 'ప', 'फ': 'ఫ', 'ब': 'బ', 'भ': 'భ', 'म': 'మ',
        'य': 'య', 'र': 'ర', 'ल': 'ల', 'व': 'వ', 'श': 'శ',
        'ष': 'ష', 'स': 'స', 'ह': 'హ',
        '०': '౦', '१': '౧', '२': '౨', '३': '౩', '४': '౪',
        '५': '౫', '६': '౬', '७': '౭', '८': '౮', '९': '౯',
        ',': ',', '.': '.', '?': '?', '!': '!', ':': ':', ';': ';',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Telugu using the mapping dictionary
    output_text = ''.join(hindi_to_telugu_mapping.get(char, char) for char in input_text)
    return output_text

def hindi_to_urdu(input_text):
    # Basic mapping from Hindi Devanagari characters to Urdu script
    hindi_to_urdu_mapping = {
        'अ': 'ا', 'आ': 'آ', 'इ': 'اِ', 'ई': 'اَ', 'उ': 'اُ', 'ऊ': 'وُ',
        'ऋ': 'ٻ', 'ए': 'اے', 'ऐ': 'ٺ', 'ओ': 'او', 'औ': 'اَو',
        'क': 'ک', 'ख': 'کھ', 'ग': 'گ', 'घ': 'گھ', 'ङ': 'ں',
        'च': 'چ', 'छ': 'چھ', 'ज': 'ج', 'झ': 'جھ', 'ञ': 'ں',
        'ट': 'ٹ', 'ठ': 'ٹھ', 'ड': 'ڈ', 'ढ': 'ڈھ', 'ण': 'ں',
        'त': 'ت', 'थ': 'تھ', 'द': 'د', 'ध': 'دھ', 'न': 'ن',
        'प': 'پ', 'फ': 'پھ', 'ब': 'ب', 'भ': 'بھ', 'म': 'م',
        'य': 'ی', 'र': 'ر', 'ल': 'ل', 'व': 'و', 'श': 'ش',
        'ष': 'ش', 'स': 'س', 'ह': 'ہ',
        '०': '٠', '१': '١', '२': '٢', '३': '٣', '४': '٤',
        '५': '٥', '६': '٦', '७': '٧', '८': '٨', '९': '٩',
        '","': '،', '.': '۔', '?': '؟', '!': '!', '":"': '۔', ';': '؛',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
        '"': '"', "'": "'", '`': '`', '-': '-', '_': '_',
        '<': '<', '>': '>', '/': '/', '\\': '\\', '|': '|', '&': '&',
        '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '*': '*',
        '+': '+', '=': '=', '~': '~'
    }
    
    # Convert input_text from Hindi to Urdu using the mapping dictionary
    output_text = ''.join(hindi_to_urdu_mapping.get(char, char) for char in input_text)
    return output_text


input_text = '''
{
    "meta": {
      "file_name": "avrodict.json",
      "file_description": "Provides Avro Dictionary in JSON. Adapted from avro-lib.js",
      "package": "pyAvroPhonetic",
      "license": "MIT 1.1 License",
      "source": "https://raw.github.com/torifat/jsAvroPhonetic/master/src/avro-lib.js",
      "original_code": "jsAvroPhonetic",
      "initial_developer": "Rifat Nabi <to.rifat@gmail.com>",
      "copyright": "Copyright (C) Omicronlab (http://www.omicronlab.com). All Rights Reserved.",
      "modified_by": "Subrata Sarkar <subrotosarkar32@gmail.com",
      "updated": "20160120",
      "encoding": "utf-8"
    },
    "data": {
      "patterns": [
        {
          "find": "bhl",
          "replace": "भ्ल"
        },
        {
          "find": "psh",
          "replace": "पश"
        },
        {
          "find": "bdh",
          "replace": "ब्ध"
        },
        {
          "find": "bj",
          "replace": "व्ज"
        },
        {
          "find": "bd",
          "replace": "ब्द"
        },
        {
          "find": "bb",
          "replace": "ब्ब"
        },
        {
          "find": "bl",
          "replace": "ब्ल"
        },
        {
          "find": "bh",
          "replace": "भ"
        },
        {
          "find": "vl",
          "replace": "व्ल"
        },
        {
          "find": "b",
          "replace": "ब"
        },
        {
          "find": "v",
          "replace": "भ"
        },
        {
          "find": "cNG",
          "replace": "च्ञ"
        },
        {
          "find": "cch",
          "replace": "च्छ"
        },
        {
          "find": "cc",
          "replace": "च्च"
        },
        {
          "find": "ch",
          "replace": "छ"
        },
        {
          "find": "c",
          "replace": "च"
        },
        {
          "find": "dhn",
          "replace": "ध्न"
        },
        {
          "find": "dhm",
          "replace": "ध्म"
        },
        {
          "find": "dgh",
          "replace": "द्घ"
        },
        {
          "find": "ddh",
          "replace": "द्ध"
        },
        {
          "find": "dbh",
          "replace": "द्भ"
        },
        {
          "find": "dv",
          "replace": "द्भ"
        },
        {
          "find": "dm",
          "replace": "द्म"
        },
        {
          "find": "DD",
          "replace": "द्द"
        },
        {
          "find": "Dh",
          "replace": "ध"
        },
        {
          "find": "dh",
          "replace": "ध"
        },
        {
          "find": "dg",
          "replace": "द्ग"
        },
        {
          "find": "dd",
          "replace": "द्द"
        },
        {
          "find": "D",
          "replace": "ड"
        },
        {
          "find": "d",
          "replace": "द"
        },
        {
          "find": "...",
          "replace": "..."
        },
        {
          "find": ".`",
          "replace": "."
        },
        {
          "find": "..",
          "replace": "॥"
        },
        {
          "find": ".",
          "replace": "।"
        },
        {
          "find": "ghn",
          "replace": "घ्न"
        },
        {
          "find": "Ghn",
          "replace": "घ्न"
        },
        {
          "find": "gdh",
          "replace": "ग्ध"
        },
        {
          "find": "Gdh",
          "replace": "ग्ध"
        },
        {
          "find": "gN",
          "replace": "ग्ण"
        },
        {
          "find": "GN",
          "replace": "ग्ण"
        },
        {
          "find": "gn",
          "replace": "ग्न"
        },
        {
          "find": "Gn",
          "replace": "ग्न"
        },
        {
          "find": "gm",
          "replace": "ग्म"
        },
        {
          "find": "Gm",
          "replace": "ग्म"
        },
        {
          "find": "gl",
          "replace": "ग्ल"
        },
        {
          "find": "Gl",
          "replace": "ग्ल"
        },
        {
          "find": "gg",
          "replace": "ज्ञ"
        },
        {
          "find": "GG",
          "replace": "ज्ञ"
        },
        {
          "find": "Gg",
          "replace": "ज्ञ"
        },
        {
          "find": "gG",
          "replace": "ज्ञ"
        },
        {
          "find": "gh",
          "replace": "घ"
        },
        {
          "find": "Gh",
          "replace": "घ"
        },
        {
          "find": "g",
          "replace": "ग"
        },
        {
          "find": "G",
          "replace": "ग"
        },
        {
          "find": "hN",
          "replace": "ह्ण"
        },
        {
          "find": "hn",
          "replace": "ह्न"
        },
        {
          "find": "hm",
          "replace": "ह्म"
        },
        {
          "find": "hl",
          "replace": "ह्ल"
        },
        {
          "find": "h",
          "replace": "ह"
        },
        {
          "find": "jjh",
          "replace": "ज्झ"
        },
        {
          "find": "jNG",
          "replace": "ज्ञ"
        },
        {
          "find": "jh",
          "replace": "झ"
        },
        {
          "find": "jj",
          "replace": "ज्ज"
        },
        {
          "find": "j",
          "replace": "ज"
        },
        {
          "find": "J",
          "replace": "ज"
        },
        {
          "find": "kkhN",
          "replace": "क्ष्ण"
        },
        {
          "find": "kShN",
          "replace": "क्ष्ण"
        },
        {
          "find": "kkhm",
          "replace": "क्ष्म"
        },
        {
          "find": "kShm",
          "replace": "क्ष्म"
        },
        {
          "find": "kxN",
          "replace": "क्ष्ण"
        },
        {
          "find": "kxm",
          "replace": "क्ष्भ"
        },
        {
          "find": "kkh",
          "replace": "क्ष"
        },
        {
          "find": "kSh",
          "replace": "क्ष"
        },
        {
          "find": "ksh",
          "replace": "कश"
        },
        {
          "find": "kx",
          "replace": "क्ष"
        },
        {
          "find": "kk",
          "replace": "क्क"
        },
        {
          "find": "kT",
          "replace": "क्ट"
        },
        {
          "find": "kt",
          "replace": "क्त"
        },
        {
          "find": "kl",
          "replace": "क्ल"
        },
        {
          "find": "ks",
          "replace": "क्स"
        },
        {
          "find": "kh",
          "replace": "ख"
        },
        {
          "find": "k",
          "replace": "क"
        },
        {
          "find": "lbh",
          "replace": "ल्भ"
        },
        {
          "find": "ldh",
          "replace": "ल्ध"
        },
        {
          "find": "lkh",
          "replace": "लख"
        },
        {
          "find": "lgh",
          "replace": "लघ"
        },
        {
          "find": "lph",
          "replace": "लफ"
        },
        {
          "find": "lk",
          "replace": "ल्क"
        },
        {
          "find": "lg",
          "replace": "ल्ग"
        },
        {
          "find": "lT",
          "replace": "ल्ट"
        },
        {
          "find": "lD",
          "replace": "ल्ड"
        },
        {
          "find": "lp",
          "replace": "ल्प"
        },
        {
          "find": "lv",
          "replace": "ल्भ"
        },
        {
          "find": "lm",
          "replace": "ल्म"
        },
        {
          "find": "ll",
          "replace": "ल्ल"
        },
        {
          "find": "lb",
          "replace": "ल्ब"
        },
        {
          "find": "l",
          "replace": "ल"
        },
        {
          "find": "mth",
          "replace": "म्थ"
        },
        {
          "find": "mph",
          "replace": "म्फ"
        },
        {
          "find": "mbh",
          "replace": "म्भ"
        },
        {
          "find": "mpl",
          "replace": "मप्ल"
        },
        {
          "find": "mn",
          "replace": "म्न"
        },
        {
          "find": "mp",
          "replace": "म्प"
        },
        {
          "find": "mv",
          "replace": "म्भ"
        },
        {
          "find": "mm",
          "replace": "म्म"
        },
        {
          "find": "ml",
          "replace": "म्ल"
        },
        {
          "find": "mb",
          "replace": "म्ब"
        },
        {
          "find": "mf",
          "replace": "म्फ"
        },
        {
          "find": "m",
          "replace": "म"
        },
        {
          "find": "0",
          "replace": "०"
        },
        {
          "find": "1",
          "replace": "१"
        },
        {
          "find": "2",
          "replace": "२"
        },
        {
          "find": "3",
          "replace": "३"
        },
        {
          "find": "4",
          "replace": "४"
        },
        {
          "find": "5",
          "replace": "५"
        },
        {
          "find": "6",
          "replace": "६"
        },
        {
          "find": "7",
          "replace": "७"
        },
        {
          "find": "8",
          "replace": "८"
        },
        {
          "find": "9",
          "replace": "९"
        },
        {
          "find": "NgkSh",
          "replace": "ङ्क्ष"
        },
        {
          "find": "Ngkkh",
          "replace": "ङ्क्ष"
        },
        {
          "find": "NGch",
          "replace": "ञ्छ"
        },
        {
          "find": "Nggh",
          "replace": "ङ्घ"
        },
        {
          "find": "Ngkh",
          "replace": "ङ्ख"
        },
        {
          "find": "NGjh",
          "replace": "ञ्झ"
        },
        {
          "find": "ngOU",
          "replace": "ङ्गौ"
        },
        {
          "find": "ngOI",
          "replace": "ङ्गै"
        },
        {
          "find": "Ngkx",
          "replace": "ङ्क्ष"
        },
        {
          "find": "NGc",
          "replace": "ञ्च"
        },
        {
          "find": "nch",
          "replace": "ञ्छ"
        },
        {
          "find": "njh",
          "replace": "ञ्झ"
        },
        {
          "find": "ngh",
          "replace": "ङ्घ"
        },
        {
          "find": "Ngk",
          "replace": "ङ्क"
        },
        {
          "find": "Ngx",
          "replace": "ङ्ष"
        },
        {
          "find": "Ngg",
          "replace": "ङ्ग"
        },
        {
          "find": "Ngm",
          "replace": "ङ्म"
        },
        {
          "find": "NGj",
          "replace": "ञ्ज"
        },
        {
          "find": "ndh",
          "replace": "न्ध"
        },
        {
          "find": "nTh",
          "replace": "न्ठ"
        },
        {
          "find": "NTh",
          "replace": "ण्ठ"
        },
        {
          "find": "nth",
          "replace": "न्थ"
        },
        {
          "find": "nkh",
          "replace": "ग़्ख"
        },
        {
          "find": "ngo",
          "replace": "ग़्ग"
        },
        {
          "find": "nga",
          "replace": "ग़्गा"
        },
        {
          "find": "ngi",
          "replace": "ग़्गि"
        },
        {
          "find": "ngI",
          "replace": "ग़्गी"
        },
        {
          "find": "ngu",
          "replace": "ग़्गु"
        },
        {
          "find": "ngU",
          "replace": "ग़्गू"
        },
        {
          "find": "nge",
          "replace": "ग़्गे"
        },
        {
          "find": "ngO",
          "replace": "ग़्गो"
        },
        {
          "find": "NDh",
          "replace": "ण्ढ"
        },
        {
          "find": "nsh",
          "replace": "नश"
        },
        {
          "find": "Ngr",
          "replace": "ङर"
        },
        {
          "find": "NGr",
          "replace": "ञर"
        },
        {
          "find": "ngr",
          "replace": "ंर"
        },
        {
          "find": "nj",
          "replace": "ञ्ज"
        },
        {
          "find": "Ng",
          "replace": "ङ"
        },
        {
          "find": "NG",
          "replace": "ञ"
        },
        {
          "find": "nk",
          "replace": "ङ्क"
        },
        {
          "find": "ng",
          "replace": "ं"
        },
        {
          "find": "nn",
          "replace": "न्न"
        },
        {
          "find": "NN",
          "replace": "ण्ण"
        },
        {
          "find": "Nn",
          "replace": "ण्न"
        },
        {
          "find": "nm",
          "replace": "न्म"
        },
        {
          "find": "Nm",
          "replace": "ण्म"
        },
        {
          "find": "nd",
          "replace": "न्द"
        },
        {
          "find": "nT",
          "replace": "न्ट"
        },
        {
          "find": "NT",
          "replace": "ण्ट"
        },
        {
          "find": "nD",
          "replace": "न्ड"
        },
        {
          "find": "ND",
          "replace": "ण्ड"
        },
        {
          "find": "nt",
          "replace": "न्त"
        },
        {
          "find": "ns",
          "replace": "न्स"
        },
        {
          "find": "nc",
          "replace": "ञ्च"
        },
        {
          "find": "n",
          "replace": "न"
        },
        {
          "find": "N",
          "replace": "ण"
        },
        {
          "find": "OI`",
          "replace": "ै"
        },
        {
          "find": "OU`",
          "replace": "ौ"
        },
        {
          "find": "O`",
          "replace": "ो"
        },
        {
          "find": "OI",
          "replace": "ै",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                }
              ],
              "replace": "ऐ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "ऐ"
            }
          ]
        },
        {
          "find": "OU",
          "replace": "ौ",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                }
              ],
              "replace": "औ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "औ"
            }
          ]
        },
        {
          "find": "O",
          "replace": "ो",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                }
              ],
              "replace": "ओ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "ओ"
            }
          ]
        },
        {
          "find": "phl",
          "replace": "फ्ल"
        },
        {
          "find": "pT",
          "replace": "प्ट"
        },
        {
          "find": "pt",
          "replace": "प्त"
        },
        {
          "find": "pn",
          "replace": "प्न"
        },
        {
          "find": "pp",
          "replace": "प्प"
        },
        {
          "find": "pl",
          "replace": "प्ल"
        },
        {
          "find": "ps",
          "replace": "प्स"
        },
        {
          "find": "ph",
          "replace": "फ"
        },
        {
          "find": "fl",
          "replace": "फ्ल"
        },
        {
          "find": "f",
          "replace": "फ"
        },
        {
          "find": "p",
          "replace": "प"
        },
        {
          "find": "rri`",
          "replace": "ृ"
        },
        {
          "find": "rri",
          "replace": "ृ",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                }
              ],
              "replace": "ऋ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "ऋ"
            }
          ]
        },
        {
          "find": "rrZ",
          "replace": "रर्य"
        },
        {
          "find": "rry",
          "replace": "रर्य"
        },
        {
          "find": "rZ",
          "replace": "र्य",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "consonant"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "r"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "y"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "w"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "x"
                }
              ],
              "replace": "्र्य"
            }
          ]
        },
        {
          "find": "ry",
          "replace": "र्य",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "consonant"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "r"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "y"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "w"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "x"
                }
              ],
              "replace": "्र्य"
            }
          ]
        },
        {
          "find": "rr",
          "replace": "रर",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!vowel"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "r"
                },
                {
                  "type": "suffix",
                  "scope": "!punctuation"
                }
              ],
              "replace": "र्"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "consonant"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "r"
                }
              ],
              "replace": "्रर"
            }
          ]
        },
        {
          "find": "Rg",
          "replace": "ड़्ग"
        },
        {
          "find": "Rh",
          "replace": "ढ़"
        },
        {
          "find": "R",
          "replace": "ड़"
        },
        {
          "find": "r",
          "replace": "र",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "consonant"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "r"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "y"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "w"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "x"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "Z"
                }
              ],
              "replace": "्र"
            }
          ]
        },
        {
          "find": "shch",
          "replace": "श्छ"
        },
        {
          "find": "ShTh",
          "replace": "ष्ठ"
        },
        {
          "find": "Shph",
          "replace": "ष्फ"
        },
        {
          "find": "Sch",
          "replace": "श्छ"
        },
        {
          "find": "skl",
          "replace": "स्क्ल"
        },
        {
          "find": "skh",
          "replace": "स्ख"
        },
        {
          "find": "sth",
          "replace": "स्थ"
        },
        {
          "find": "sph",
          "replace": "स्फ"
        },
        {
          "find": "shc",
          "replace": "श्च"
        },
        {
          "find": "sht",
          "replace": "श्त"
        },
        {
          "find": "shn",
          "replace": "श्न"
        },
        {
          "find": "shm",
          "replace": "श्म"
        },
        {
          "find": "shl",
          "replace": "श्ल"
        },
        {
          "find": "Shk",
          "replace": "ष्क"
        },
        {
          "find": "ShT",
          "replace": "ष्ट"
        },
        {
          "find": "ShN",
          "replace": "ष्ण"
        },
        {
          "find": "Shp",
          "replace": "ष्प"
        },
        {
          "find": "Shf",
          "replace": "ष्फ"
        },
        {
          "find": "Shm",
          "replace": "ष्म"
        },
        {
          "find": "spl",
          "replace": "स्प्ल"
        },
        {
          "find": "sk",
          "replace": "स्क"
        },
        {
          "find": "Sc",
          "replace": "श्च"
        },
        {
          "find": "sT",
          "replace": "स्ट"
        },
        {
          "find": "st",
          "replace": "स्त"
        },
        {
          "find": "sn",
          "replace": "स्न"
        },
        {
          "find": "sp",
          "replace": "स्प"
        },
        {
          "find": "sf",
          "replace": "स्फ"
        },
        {
          "find": "sm",
          "replace": "स्म"
        },
        {
          "find": "sl",
          "replace": "स्ल"
        },
        {
          "find": "sh",
          "replace": "श"
        },
        {
          "find": "Sc",
          "replace": "श्च"
        },
        {
          "find": "St",
          "replace": "श्त"
        },
        {
          "find": "Sn",
          "replace": "श्न"
        },
        {
          "find": "Sm",
          "replace": "श्म"
        },
        {
          "find": "Sl",
          "replace": "श्ल"
        },
        {
          "find": "Sh",
          "replace": "ष"
        },
        {
          "find": "s",
          "replace": "स"
        },
        {
          "find": "S",
          "replace": "श"
        },
        {
          "find": "oo`",
          "replace": "ु"
        },
        {
          "find": "oo",
          "replace": "ु",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "उ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "उ"
            }
          ]
        },
        {
          "find": "o`",
          "replace": ""
        },
        {
          "find": "oZ",
          "replace": "अ्य"
        },
        {
          "find": "o",
          "replace": "",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "vowel"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "o"
                }
              ],
              "replace": "उ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "vowel"
                },
                {
                  "type": "prefix",
                  "scope": "exact",
                  "value": "o"
                }
              ],
              "replace": "अ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "अ"
            }
          ]
        },
        {
          "find": "tth",
          "replace": "त्थ"
        },
        {
          "find": "t``",
          "replace": "त्"
        },
        {
          "find": "TT",
          "replace": "ट्ट"
        },
        {
          "find": "Tm",
          "replace": "ट्म"
        },
        {
          "find": "Th",
          "replace": "ठ"
        },
        {
          "find": "tn",
          "replace": "त्न"
        },
        {
          "find": "tm",
          "replace": "त्म"
        },
        {
          "find": "th",
          "replace": "थ"
        },
        {
          "find": "tt",
          "replace": "त्त"
        },
        {
          "find": "T",
          "replace": "ट"
        },
        {
          "find": "t",
          "replace": "त"
        },
        {
          "find": "aZ",
          "replace": "अ्या"
        },
        {
          "find": "AZ",
          "replace": "अ्या"
        },
        {
          "find": "a`",
          "replace": "ा"
        },
        {
          "find": "A`",
          "replace": "ा"
        },
        {
          "find": "a",
          "replace": "ा",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "आ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "prefix",
                  "scope": "!exact",
                  "value": "a"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "या"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "exact",
                  "value": "a"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "आ"
            }
          ]
        },
        {
          "find": "i`",
          "replace": "ि"
        },
        {
          "find": "i",
          "replace": "ि",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "इ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "इ"
            }
          ]
        },
        {
          "find": "I`",
          "replace": "ी"
        },
        {
          "find": "I",
          "replace": "ी",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ई"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ई"
            }
          ]
        },
        {
          "find": "u`",
          "replace": "ु"
        },
        {
          "find": "u",
          "replace": "ु",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "उ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "उ"
            }
          ]
        },
        {
          "find": "U`",
          "replace": "ू"
        },
        {
          "find": "U",
          "replace": "ू",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ऊ"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ऊ"
            }
          ]
        },
        {
          "find": "ee`",
          "replace": "ी"
        },
        {
          "find": "ee",
          "replace": "ी",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ई"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ई"
            }
          ]
        },
        {
          "find": "e`",
          "replace": "॔"
        },
        {
          "find": "e",
          "replace": "े",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ए"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "!exact",
                  "value": "`"
                }
              ],
              "replace": "ए"
            }
          ]
        },
        {
          "find": "z",
          "replace": "य"
        },
        {
          "find": "Z",
          "replace": "्य"
        },
        {
          "find": "y",
          "replace": "्य",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "!consonant"
                },
                {
                  "type": "prefix",
                  "scope": "!punctuation"
                }
              ],
              "replace": "य"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "इय"
            }
          ]
        },
        {
          "find": "Y",
          "replace": "य"
        },
        {
          "find": "q",
          "replace": "क"
        },
        {
          "find": "w",
          "replace": "ओ",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                },
                {
                  "type": "suffix",
                  "scope": "vowel"
                }
              ],
              "replace": "ओय"
            },
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "consonant"
                }
              ],
              "replace": "्व"
            }
          ]
        },
        {
          "find": "x",
          "replace": "क्स",
          "rules": [
            {
              "matches": [
                {
                  "type": "prefix",
                  "scope": "punctuation"
                }
              ],
              "replace": "एक्स"
            }
          ]
        },
        {
          "find": ":`",
          "replace": ":"
        },
        {
          "find": ":",
          "replace": "ः"
        },
        {
          "find": "^`",
          "replace": "^"
        },
        {
          "find": "^",
          "replace": "ं"
        },
        {
          "find": ",,",
          "replace": "্‌"
        },
        {
          "find": ",",
          "replace": ","
        },
        {
          "find": "$",
          "replace": "₹"
        },
        {
          "find": "`",
          "replace": ""
        }
      ],
      "vowel": "aeiou",
      "consonant": "bcdfghjklmnpqrstvwxyz",
      "casesensitive": "oiudgjnrstyz",
      "number": "0123456789"
    }
  }
'''
print(hindi_to_urdu(input_text))