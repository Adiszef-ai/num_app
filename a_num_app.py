import streamlit as st
import os
from PIL import Image
import datetime
import calendar



####################################################################################################
#                                           UPLOAD FILES   
#                                   
####################################            MAINS           ####################################
#                                          
main_path = "./img_main"
main_jpg = [f for f in os.listdir(main_path) if f.endswith('.jpg')]
imag = {os.path.splitext(plik)[0]: Image.open(
    os.path.join(main_path, plik)) for plik in main_jpg}

m1 = imag["main1"]
m2 = imag["main2"]
m3 = imag["main3"]

####################################          NUMBERS          #####################################                                          NUMBERS
#
num_path = "./img_num"
num_jpg = [f for f in os.listdir(num_path) if f.endswith('.jpg')]
obrazy = {os.path.splitext(plik)[0]: Image.open(
    os.path.join(num_path, plik)) for plik in num_jpg}

a1 = obrazy["a1"]
a2 = obrazy["a2"]
a3 = obrazy["a3"]
a4 = obrazy["a4"]
a5 = obrazy["a5"]
a6 = obrazy["a6"]
a7 = obrazy["a7"]
a8 = obrazy["a8"]
a9 = obrazy["a9"]
a11 = obrazy["a11"]
a22 = obrazy["a22"]
a33 = obrazy["a33"]
a44 = obrazy["a44"]


####################################        RESOLUTION      #################################   
#
n_wi = 1280
n_he = 720
st.markdown(
    """
    <style>
/* Zaokrąglone obrazki */
img {
    border-radius: 20px;
    border: 2px solid #ffd900; /* Czarna ramka o grubości 2px */
}
    </style>
    """,
    unsafe_allow_html=True
)

###################################        Portal Wiedzy       ###################################

st.write('\n')
st.markdown(
    """
    <h1 style="font-size: 60px; font-weight: bold; text-align: center; color: #ffd900;">
    Portal Wiedzy
    </h1>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)

resized_img = m1.resize((n_wi, n_he))
st.image(resized_img)

st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)

st.write('''⁎˚⭑✧₊ 🍄 Witaj w miejscu, gdzie starożytna mądrość spotyka współczesne potrzeby.''') 

st.write('''Zebrany tutaj zbiór wiedzy jest po to, by dostarczyć Ci narzędzi opartych na wielowiekowej tradycji ezoterycznej: 
astrologii zachodniej, numerologii, chińskiej filozofii, a także wiedzy o żywiołach i ich wpływie na Twoje życie.''') 

st.write('''Dzięki tej wiedzy możesz odkryć głębokie tajemnice swojej duszy i połączyć się z kosmiczną harmonią wszechświata. 
Poznasz siebie lepiej, zrozumiesz swoje miejsce w świecie i odkryjesz potencjał, który od zawsze był w Tobie ukryty.
Każda z tych dziedzin jest jak mapa, która prowadzi do odkrycia Twojej wewnętrznej prawdy.''')

st.write('''Co zyskasz korzystając z tych możliwości?  ˚₊💎₊˚ 
- Głębsze zrozumienie swojej osobowości i ukrytych talentów.
- Wskazówki, jak wzmocnić swoje mocne strony i pracować nad wyzwaniami.
- Harmonię w codziennym życiu dzięki lepszemu wykorzystaniu energii żywiołów.
- Prognozy i porady dostosowane do Twojej indywidualnej drogi.

To miejsce jest dla każdego, kto pragnie poznać siebie na nowo, spojrzeć na swoje życie z innej perspektywy 
i wykorzystać tę wiedzę, aby tworzyć lepszą przyszłość. Wejdź, odkrywaj i pozwól, aby starożytna mądrość poprowadziła Cię ku samorealizacji. ⭐ ‧✧₊˚ ''')




##############################################################################################
#
######################################       NUMEROLOGIA      #############################
 

st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <h1 style="font-size: 60px; font-weight: bold; text-align: center; color: #ffd900;">
    Numerologia
    </h1>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)
resized_img = m2.resize((n_wi, n_he))
st.image(resized_img)

st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)       

####################################            OPIS NUM             ############################


st.write('''˚✧₊⁎ 🍃 Numerologia – Klucz do Twojej Wewnętrznej Harmonii** 
Czy wiesz, że każda data urodzenia kryje w sobie tajemniczy kod, który prowadzi do poznania 
Twojego życiowego celu? Numerologia to starożytna sztuka odkrywania znaczenia ukrytego w liczbach, która od wieków fascynuje ludzi na całym świecie. ''')  

st.write('''Twoja liczba urodzeniowa to nie tylko suchy wynik obliczeń – to brama do zrozumienia siebie, Twojej ścieżki i potencjału, który nosisz w sobie.  ₊˚🌟˚₊  
- Co mówi o Tobie Twoja liczba?  
- Jakie talenty zostały Ci przypisane już od dnia Twoich narodzin?  
- Jakie wyzwania są częścią Twojej drogi?''')
    
st.write('''Numerologia to jak tajemny kompas, który wskazuje kierunek Twojego życia. 
Dzięki niej dowiesz się, jakie energie i cechy są z Tobą od samego początku, i jak możesz je najlepiej wykorzystać w codziennym życiu.''')  
st.write('''Każda liczba niesie ze sobą unikalne wibracje i przesłanie, które mogą pomóc Ci zrozumieć:  
- Twoje relacje z innymi ludźmi.  
- Twoją zdolność do realizacji marzeń.  
- Twoje największe wyzwania i lekcje do przepracowania.''')  
st.write('''₊⁎✧✨Czy jesteś gotów odkryć, jaką liczbą jesteś i co to oznacza dla Twojej przyszłości? Wprowadź datę swoich narodzin, a numerologia odsłoni przed Tobą swoją pradawną mądrość.📜‧✧₊˚''')
    
###########################################################################################
    
######################################       WIDŻETY   DATY       ##############################
# 
#        
st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <p style="font-size: 25px; font-weight: bold; text-align: left; color: #ffd900;">
    Podaj date urodzenia
    </p>
    """,
    unsafe_allow_html=True
)  

today = st.session_state.get("today", None) or calendar.datetime.date.today()
hundred_years_ago = today.year - 100
years = list(range(hundred_years_ago, today.year + 1))
# Widżet do wyboru roku
selected_year = st.selectbox("Wybierz rok:", options=years, key="year")
# Lista miesięcy
months = [
    "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
    "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
]
# Widżet do wyboru miesiąca (po wybraniu roku)
selected_month = st.selectbox(
    "Wybierz miesiąc:", 
    options=range(1, 13), 
    format_func=lambda x: months[x-1], 
    key="month"
)
# Funkcja do określenia maksymalnej liczby dni w miesiącu
def get_days_in_month(year, month):
    return calendar.monthrange(year, month)[1]
# Liczba dni w wybranym miesiącu
max_days = get_days_in_month(selected_year, selected_month)
# Widżet do wyboru dnia (po wybraniu miesiąca)
selected_day = st.selectbox("Wybierz dzień:", options=range(1, max_days + 1), key="day")
# Wyświetlenie wybranej daty w polskim formacie
selected_date = datetime.date(selected_year, selected_month, selected_day)
# Sprawdź, czy w session_state już jest selected_date, jeśli nie, zainicjalizuj
if 'selected_date' not in st.session_state:
    st.session_state.selected_date = None



###########################################         Efekt Tosta     ###################################    
#
#
def custom_toast(message, icon="🎉", duration=5000):
    st.markdown(
        f"""
        <style>
        @keyframes fade-out {{
            0% {{ opacity: 1; }}
            90% {{ opacity: 1; }}
            100% {{ opacity: 0; }}
        }}

        #custom-toast {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
            text-align: center;
            z-index: 1000;
            opacity: 1;
            animation: fade-out {duration/1000}s ease-in-out forwards;
        }}
        </style>
        <div id="custom-toast">
            <div style="font-size: 60px; line-height: 1;">{icon}</div>
            <div style="font-size: 24px; font-weight: bold; margin-top: 10px;">{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


#####################################          Styl dla przycisku      #########################
#
# 
st.markdown("""
    <style>
    div.stButton > button {
        font-size: 20px !important;
        background-color: #ffd900;
        color: #3a4050;
        border-radius: 10px;
        height: 30px; /* Dopasuj wysokość do potrzeb */
        width: 100px; /* Dopasuj szerokość do potrzeb */
        display: flex;
        justify-content: center;
        align-items: center;
        transition: background-color 0.6s ease, color 0.6s ease; /* Płynne przejście kolorów */
    }
    div.stButton > button:hover {
        background-color: #1e1e20; /* Kolor tła przy podświetleniu */
        color: #ffd700; /* Kolor tekstu przy podświetleniu */
    }
    div.stButton > button:active {
        color: #ffd700; /* Kolor tekstu przy naciśnięciu */
        background-color: #3a4050; /* Opcjonalnie zmień tło przy naciśnięciu */
    }
    </style>
""", unsafe_allow_html=True)

##########################################       WYLICZONA NUMEROLOGIA         ###########################

# Inicjalizacja stanu
if 'final_number' not in st.session_state:
    st.session_state.final_number = None

if 'selected_date' not in st.session_state:
    st.session_state.selected_date = None

if "calculate_clicked" not in st.session_state:
    st.session_state.calculate_clicked = False

# Przyciski
if st.button("**Oblicz**"):
    st.session_state.selected_date = selected_date
    st.session_state.calculate_clicked = True

st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

# Przetwarzanie daty
if st.session_state.selected_date:
    selected_date = st.session_state.selected_date
    st.markdown(f"Podana data: {st.session_state.selected_date.strftime('%Y.%m.%d')}")
    st.session_state.selected_date = False
    
    digits = ''.join(str(selected_date.year) + str(selected_date.month).zfill(2) + str(selected_date.day).zfill(2))
    digit_list = [int(digit) for digit in digits]

    st.markdown(f"Rozbijamy datę na pojedyńcze cyfry:")
    st.markdown(f"{' + '.join(map(str, digit_list))}")

    def reduce_number(number):
        while number > 9 and number not in {11, 22, 33, 44}:
            digits = [int(digit) for digit in str(number)]
            number = sum(digits)
            st.markdown(f"{' + '.join(map(str, digits))}")
        return number

    initial_sum = sum(digit_list)
    st.markdown(f"Początkowa suma cyfr: {initial_sum}")

    final_number = reduce_number(initial_sum)
    st.session_state.final_number = final_number

# Wyświetlanie wyniku i toast
if st.session_state.calculate_clicked:
    custom_toast(f"Numerologiczna {st.session_state.final_number}", icon="🎉", duration=5000)
    st.session_state.calculate_clicked = False
    # st.success(f"**{st.session_state.final_number}**")

    


########################################################################################

##################################     OPIS 1       ##############################
#                                    
#    
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    file_a = "num_a.txt"   
    col1, col2 = st.columns([2,2])
    n_width = 400
    n_height = 400
    images = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a11, a22, a33, a44]
    number_to_index = {
            1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8,
            11: 9, 22: 10, 33: 11, 44: 12
        }
    with col1:
        st.markdown(
    f"""
    <p style="font-size: 38px; font-weight: bold; text-align: left; color: #ffd900;">
    Numerologiczna {final_number}
    </p>
    """,
    unsafe_allow_html=True
)  

        

        def get_numerology_description(file_a, final_number):
            """
            Wczytuje i zwraca opis numerologiczny dla podanego numeru z pliku. 
            :param file_path: Ścieżka do pliku tekstowego.
            :param final_number: Numer dla którego szukamy opisu.
            :return: Fragment tekstu pasujący do numeru lub komunikat o błędzie.
            """
            with open(file_a, "r", encoding="utf-8") as file:
                content = file.read()

            sections = content.split("@")
            
            # Iteracja po fragmentach i sprawdzenie, czy pasują do wybranego numeru
            for section in sections:
                    lines = section.strip().split("\n")
                    if lines and lines[0] == f'"{final_number}"':  # Dopasowanie numeru z cudzysłowami
                        return "\n".join(lines[1:]).strip()  # Zwróć resztę sekcji bez numeru
            
            # Jeśli nie znaleziono dopasowania, zwraca informację
            return f"Nie znaleziono opisu dla numeru: {final_number}"

        description = get_numerology_description(file_a, final_number)   
        st.text(description)
    with col2:
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)

        if final_number in number_to_index:  # Sprawdzenie, czy final_number istnieje w mapowaniu
            index = number_to_index[final_number]
            resized_image = images[index].resize((n_width, n_height))
            st.image(resized_image)
        else:
            st.write("Brak obrazu dla wybranego numeru.")

#####################################      OPIS 2       #######################################################
#
    # st.markdown('<div style="height: 15px;"></div>', unsafe_allow_html=True)
    file_b = "num_b.txt"
    def get_numerology_description(file_b, final_number):
        """
        Wczytuje i zwraca opis numerologiczny dla podanego numeru z pliku. 
        :param file_path: Ścieżka do pliku tekstowego.
        :param final_number: Numer dla którego szukamy opisu.
        :return: Fragment tekstu pasujący do numeru lub komunikat o błędzie.
        """
        with open(file_b, "r", encoding="utf-8") as file:
            content = file.read()

        sections = content.split("@")
                
        # Iteracja po fragmentach i sprawdzenie, czy pasują do wybranego numeru
        for section in sections:
                lines = section.strip().split("\n")
                if lines and lines[0] == f'"{final_number}"':  # Dopasowanie numeru z cudzysłowami
                    return "\n".join(lines[1:]).strip()  # Zwróć resztę sekcji bez numeru

        # Jeśli nie znaleziono dopasowania, zwraca informację
        return f"Nie znaleziono opisu dla numeru: {final_number}"

    description = get_numerology_description(file_b, final_number)   
    st.text(description)