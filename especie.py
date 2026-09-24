import streamlit as st

# Configuración de la interfaz de la página
st.set_page_config(page_title="Guía Taxonómica Completa - Arequipa", page_icon="⛰️", layout="centered")

st.title("⛰️ Guía Taxonómica Digital de Arequipa")
st.markdown("### Conservación de Áreas Verdes Escolares y Biodiversidad Local")
st.write("Usa esta clave dicotómica interactiva para identificar las 13 especies del proyecto tecnológico sostenible.")

st.divider()

# --- SECCIÓN 1: CLAVE DICOTÓMICA INTERACTIVA ---
st.header("🔍 Identificador de Especies")
st.write("Responde las siguientes características observables para descartar e identificar tu especie:")

# Pregunta Raíz: Reino o tipo general de organismo
reino = st.radio(
    "**1. ¿Qué tipo de organismo general estás observando?**",
    options=["Selecciona una opción", "Pertenece al Reino Plantae (Plantas, flores, cactus o árboles)", "Pertenece al Reino Animalia (Mamíferos, aves, anfibios o anélidos)"]
)

if "Reino Plantae" in reino:
    # Sub-clasificación de Plantas
    tipo_planta = st.radio(
        "**2. ¿Cuál es su estructura física o forma de crecimiento principal?**",
        options=["Selecciona una opción", "Es una planta suculenta (Cactus) con espinas prominentes", "Es un árbol, arbusto o hierba con hojas o flores tradicionales"]
    )
    
    if "Cactus" in tipo_planta:
        # Distinción entre los dos cactus
        tipo_cactus = st.radio(
            "**3. ¿Cómo es la forma de crecimiento de este cactus?**",
            options=["Selecciona una opción", "Crece de forma esférica u ovoide, agrupado como pequeños cojines globosos", "Crece de forma columnar, como un cactus gigante erecto de gran altura"]
        )
        
        if "esférica" in tipo_cactus:
            st.success("¡Especie Identificada: Corotilla!")
            st.subheader("*Cumulopuntia corotilla*")
            st.image("Cumulopuntia corotilla.png", caption="Corotilla - Cactácea Nativa de Arequipa")
            st.markdown("**Importancia Ecológica:** Planta suculenta endémica clave para evitar la desertificación y retener agua en suelos áridos.")
            st.markdown("**Estado de Conservación:** No Evaluado (NE) / Preocupación Menor a nivel regional.")
            
        elif "columnar" in tipo_cactus:
            st.success("¡Especie Identificada: Cactus Gigantón!")
            st.subheader("*Neoraimondia arequipensis*")
            st.image("Neoraimondia_arequipensis.png", caption="Cactus Gigantón - Columna del desierto")
            st.markdown("**Importancia Ecológica:** Cactus columna central de interacciones ecológicas; sirve como planta nodriza y alimento en desiertos.")
            st.markdown("**Estado de Conservación:** Preocupación Menor (LC).")
        
    elif "árbol, arbusto" in tipo_planta:
        forma_planta = st.radio(
            "**3. Elige la característica específica de sus hojas, flores o forma de vida:**",
            options=[
                "Selecciona una opción", 
                "Es un árbol altoandino con tronco retorcido y corteza rojiza que se descascara en láminas",
                "Crece pegada al suelo y rocas formando un cojín verde muy denso y duro ('Almohadilla')",
                "Es una planta gigante de la puna con una inflorescencia enorme que tarda décadas en florecer",
                "Es un arbusto endémico con flores acampanadas llamativas, muy visitadas por picaflores",
                "Es una planta arbustiva desértica conocida como 'Chavelina', de hojas profundamente recortadas (pinnatisectas)",
                "Es una hierba silvestre nativa de flores pequeñas rosadas o violáceas ('Hierba Tarasa')"
            ]
        )
        
        if "árbol altoandino" in forma_planta:
            st.success("¡Especie Identificada: Queñual!")
            st.subheader("*Polylepis rugulosa*")
            st.image("Polylepis_rugulosa.png", caption="Queñual - Bosques de Altura")
            st.markdown("**Importancia Ecológica:** Forma bosques de altura que regulan el agua y previenen la erosión de las laderas.")
            st.markdown("**Estado de Conservación:** Vulnerable (VU).")
            
        elif "cojín verde" in forma_planta:
            st.success("¡Especie Identificada: Yareta!")
            st.subheader("*Azorella compacta*")
            st.image("Azorella_compacte.png", caption="Yareta - Almohadilla Altoandina")
            st.markdown("**Importancia Ecológica:** Fijadora de carbono y protectora de suelos áridos altoandinos.")
            st.markdown("**Estado de Conservación:** Casi Amenazada (NT).")
            
        elif "planta gigante" in forma_planta:
            st.success("¡Especie Identificada: Puya Raimondi!")
            st.subheader("*Puya raimondii*")
            st.image("La_Puya_Raimondi.png", caption="Puya Raimondi - Titanca")
            st.markdown("**Importancia Ecológica:** Provee refugio y néctar a aves polinizadoras en hábitats extremos.")
            st.markdown("**Estado de Conservación:** En Peligro (EN).")

        elif "flores acampanadas" in forma_planta:
            st.success("¡Especie Identificada: Abutilon de Arequipa!")
            st.subheader("*Abutilon arequipense*")
            st.image("Abutilon_arequipense.png", caption="Abutilon de Arequipa - Arbusto endémico")
            st.markdown("**Importancia Ecológica:** Arbusto endémico cuyas flores acampanadas son clave para el alimento de picaflores locales.")
            st.markdown("**Estado de Conservación:** No Evaluado (NE).")
            
        elif "Chavelina" in forma_planta:
            st.success("¡Especie Identificada: Malesherbia / Chavelina!")
            st.subheader("*Malesherbia angustisecta*")
            st.image("Malesherbia_angustisecta.png", caption="Malesherbia angustisecta - Flora endémica")
            st.markdown("**Importancia Ecológica:** Planta endémica adaptada a la aridez, vital para la diversidad florística local.")
            st.markdown("**Estado de Conservación:** En Peligro (EN).")
            
        elif "Hierba Tarasa" in forma_planta:
            st.success("¡Especie Identificada: Tarasa!")
            st.subheader("*Tarasa marianii*")
            st.image("Tarasa_marianii.png", caption="Tarasa marianii - Flora nativa")
            st.markdown("**Importancia Ecológica:** Especie pionera que ayuda a la recuperación de suelos degradados.")
            st.markdown("**Estado de Conservación:** No Evaluado (NE).")

elif "Reino Animalia" in reino:
    # Sub-clasificación de Animales
    tipo_animal = st.radio(
        "**2. ¿Qué estructura anatómica o hábitat principal presenta el animal?**",
        options=["Selecciona una opción", "Vertebrado terrestre con patas (Mamífero o Ave)", "Anfibio acuático o Invertebrado alargado sin patas"]
    )
    
    if "Vertebrado terrestre" in tipo_animal:
        forma_animal = st.radio(
            "**3. Identifícalo por su grupo o pelaje/plumaje:**",
            options=[
                "Selecciona una opción",
                "Es un ave pequeña y ágil de plumaje pardo, conocida como 'Canastero de Arequipa'",
                "Es un camélido silvestre de pelaje fino y color canela dorado, emblemático nacional",
                "Es un camélido silvestre de mayor tamaño, hocico oscuro y pelaje marrón más grueso"
            ]
        )
        
        if "ave pequeña" in forma_animal:
            st.success("¡Especie Identificada: Canastero de Arequipa!")
            st.subheader("*Asthenes arequipae*")
            st.image("Asthenes arequipae.png", caption="Canastero de Arequipa")
            st.markdown("**Importancia Ecológica:** Ave endémica que actúa como controladora de insectos en ecosistemas áridos.")
            st.markdown("**Estado de Conservación:** Preocupación Menor (LC).")
            
        elif "pelaje fino" in forma_animal:
            st.success("¡Especie Identificada: Vicuña!")
            st.subheader("*Vicugna vicugna*")
            st.image("Vicugna_vicugna.png", caption="Vicuña - Símbolo de la Fauna Peruana")
            st.markdown("**Importancia Ecológica:** Especie paraguas clave en el pastoreo estacional y la cadena trófica de la puna.")
            st.markdown("**Estado de Conservación:** Preocupación Menor (LC).")
            
        elif "mayor tamaño" in forma_animal:
            st.success("¡Especie Identificada: Guanaco!")
            st.subheader("*Lama guanicoe*")
            st.image("Lama_guanicoe.png", caption="Guanaco - Camélido Silvestre")
            st.markdown("**Importancia Ecológica:** Herbívoro nativo que dispersa semillas y mantiene el equilibrio de los pastizales.")
            st.markdown("**Estado de Conservación:** Preocupación Menor (LC) a nivel global.")

    elif "Anfibio acuático" in tipo_animal:
        forma_bajo_agua = st.radio(
            "**3. Observa su cuerpo y su entorno:**",
            options=[
                "Selecciona una opción",
                "Es un anfibio de piel húmeda que vive oculto en ríos y arroyos de la región",
                "Es un organismo anélido (gusano), alargado, blando, segmentado y vive bajo la tierra húmeda"
            ]
        )
        
        if "anfibio" in forma_bajo_agua:
            st.success("¡Especie Identificada: Rana de Arequipa!")
            st.subheader("*Telmatobius arequipensis*")
            st.image("Telmatobius_arequipensis.png", caption="Rana acuática de Arequipa")
            st.markdown("**Importancia Ecológica:** Indicadora clave de la salud y pureza de los ecosistemas acuáticos.")
            st.markdown("**Estado de Conservación:** En Peligro Crítico (CR).")
            
        elif "organismo anélido" in forma_bajo_agua:
            st.success("¡Especie Identificada: Lombriz Roja Californiana!")
            st.subheader("*Eisenia foetida*")
            st.image("Eisenia_foetida.png", caption="Lombriz Roja - Aliada del compostaje")

# --- SECCIÓN 2: PESTAÑA EXPANDIBLE CON LA TABLA TAXONÓMICA COMPLETA ---
st.divider()
st.header("📊 Documentación Científica")
with st.expander("📋 Hacer clic para ver la Tabla Taxonómica Completa"):
    st.write("Este registro contiene la jerarquía científica exacta de las 13 especies seleccionadas para la ficha del proyecto:")
    
    datos_completos = {
        "Nombre Común": [
            "Yareta", "Queñual", "Rana de Arequipa", "Vicuña", "Puya Raimondi", 
            "Corotilla", "Guanaco", "Canastero de Arequipa", "Lombriz Californiana", 
            "Malesherbia", "Tarasa", "Abutilon de Arequipa", "Cactus Gigantón"
        ],
        "Nombre Científico": [
            "Azorella compacta", "Polylepis rugulosa", "Telmatobius arequipensis", "Vicugna vicugna", "Puya raimondii", 
            "Cumulopuntia corotilla", "Lama guanicoe", "Asthenes arequipae", "Eisenia foetida", 
            "Malesherbia angustisecta", "Tarasa marianii", "Abutilon arequipense", "Neoraimondia arequipensis"
        ],
        "Dominio": ["Eukarya"] * 13,
        "Reino": [
            "Plantae", "Plantae", "Animalia", "Animalia", "Plantae", 
            "Plantae", "Animalia", "Animalia", "Animalia", 
            "Plantae", "Plantae", "Plantae", "Plantae"
        ],
        "Filo / División": [
            "Tracheophyta", "Tracheophyta", "Chordata", "Chordata", "Tracheophyta", 
            "Tracheophyta", "Chordata", "Chordata", "Annelida", 
            "Tracheophyta", "Tracheophyta", "Tracheophyta", "Tracheophyta"
        ],
        "Clase": [
            "Magnoliopsida", "Magnoliopsida", "Amphibia", "Mammalia", "Liliopsida", 
            "Magnoliopsida", "Mammalia", "Aves", "Clitellata", 
            "Magnoliopsida", "Magnoliopsida", "Magnoliopsida", "Magnoliopsida"
        ],
        "Orden": [
            "Apiales", "Rosales", "Anura", "Artiodactyla", "Poales", 
            "Caryophyllales", "Artiodactyla", "Passeriformes", "Crassiclitellata", 
            "Malpighiales", "Malvales", "Malvales", "Caryophyllales"
        ],
        "Familia": [
            "Apiaceae", "Rosaceae", "Telmatobiidae", "Camelidae", "Bromeliaceae", 
            "Cactaceae", "Camelidae", "Furnariidae", "Lumbricidae", 
            "Passifloraceae", "Malvaceae", "Malvaceae", "Cactaceae"
        ],
        "Género": [
            "Azorella", "Polylepis", "Telmatobius", "Vicugna", "Puya", 
            "Cumulopuntia", "Lama", "Asthenes", "Eisenia", 
            "Malesherbia", "Tarasa", "Abutilon", "Neoraimondia"
        ],
        "Especie": [
            "A. compacta", "P. rugulosa", "T. arequipensis", "V. vicugna", "P. raimondii", 
            "C. corotilla", "L. guanicoe", "A. arequipae", "E. foetida", 
            "M. angustisecta", "T. marianii", "A. arequipense", "N. arequipensis"
        ],
        "Importancia Ecológica": [
            "Fijadora de carbono y protectora de suelos áridos altoandinos.",
            "Forma bosques de altura que regulan el agua y previenen la erosión.",
            "Indicadora clave de la salud y pureza de los ecosistemas acuáticos.",
            "Especie paraguas clave en el pastoreo estacional y la cadena trófica de la puna.",
            "Provee refugio y néctar a aves polinizadoras en hábitats extremos.",
            "Estabiliza taludes xerofíticos y ofrece alimento a la fauna local.",
            "Herbívoro nativo que dispersa semillas y mantiene el equilibrio de los pastizales.",
            "Ave endémica que actúa como controladora de insectos en ecosistemas áridos.",
            "Descompone materia orgánica y enriquece el suelo mediante el vermicompostaje.",
            "Planta endémica adaptada a la aridez, vital para la diversidad florística local.",
            "Especie pionera que ayuda a la recuperación de suelos degradados.",
            "Arbusto endémico cuyas flores acampanadas son clave para el alimento de picaflores locales.",
            "Cactus columna central de interacciones ecológicas; sirve como planta nodriza y alimento en desiertos."
        ]
    }


# Pregunta de Sí o No para mostrar los datos
mostrar_tabla = st.checkbox("¿Deseas ver la tabla de datos completa?", value=True)
if mostrar_tabla:
    st.dataframe(datos_completos, use_container_width=True)
