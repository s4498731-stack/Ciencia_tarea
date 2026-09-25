import streamlit as st
import plotly.express as px
# Configuración de la interfaz de la página
st.set_page_config(page_title="Guía Taxonómica Completa - Arequipa", page_icon="⛰️", layout="wide")

# ==================== CONTENIDO EN LA BARRA LATERAL (SIDEBAR) ====================
st.sidebar.header("📚 Fichero de Consulta Directa")
st.sidebar.write("Selecciona cualquier especie para leer su artículo científico detallado:")

# Diccionario de artículos detallados para las 13 especies
articulos_especies = {
    "Yareta": {
        "cientifico": "Azorella compacta",
        "imagen": "Azorella_compacte.png",
        "articulo": """La **Yareta** es una de las plantas más fascinantes y resistentes de la puna andina. Crece en altitudes extremas, entre los 3,200 y 4,500 metros sobre el nivel del mar, formando cojines compactos y extremadamente duros que parecen rocas verdes. 
        
**Adaptación al clima:** Esta estructura densa le permite retener el calor corporal frente a las heladas nocturnas y reducir drásticamente la pérdida de agua por evaporación causada por los fuertes vientos altoandinos. Debido a su metabolismo extremadamente lento, crece apenas **1 a 2 centímetros por año**, lo que significa que los ejemplares grandes pueden tener más de mil años de edad.

**Amenazas:** Históricamente fue extraída masivamente para ser usada como combustible en mineras y hogares coloniales, lo que hoy la sitúa en la categoría de **Casi Amenazada (NT)**. Su conservación en las partes altas de Arequipa es vital para proteger el suelo de la erosión y servir de refugio a pequeños invertebrados."""
    },
    "Queñual": {
        "cientifico": "Polylepis rugulosa",
        "imagen": "Polylepis_rugulosa.png",
        "articulo": """El **Queñual** es el árbol que desafía las alturas. Pertenece al género *Polylepis*, famoso por albergar los bosques más altos del mundo. Su tronco retorcido está cubierto por una corteza rojiza que se descascara en múltiples láminas delgadas como el papel.

**Rol ecológico:** Esta corteza almacena aire y actúa como un aislante térmico natural contra el congelamiento. Los bosques de Queñual funcionan como "esponjas hídricas": capturan la niebla y el agua de lluvia, filtrándola suavemente hacia el subsuelo para alimentar los arroyos y bofedales que luego abastecen a las ciudades bajas.

**Amenazas:** La tala indiscriminada para carbón y la quema de pastizales han fragmentado severamente sus poblaciones, clasificándola como **Vulnerable (VU)**. Proteger al Queñual es asegurar el agua del futuro de la región."""
    },
    "Rana de Arequipa": {
        "cientifico": "Telmatobius arequipensis",
        "imagen": "Telmatobius_arequipensis.png",
        "articulo": """La **Rana de Arequipa** (o Rana del Chili) es un anfibio estrictamente acuático que habita en los ríos, torrentes y canales de los valles arequipeños. A diferencia de otros anfibios, pasa casi toda su vida sumergida, utilizando los pliegues de su piel húmeda para absorber el oxígeno del agua.

**Indicador ambiental:** Debido a que respira a través de la piel y sus huevos se desarrollan directamente en el lecho del río, es extremadamente sensible a los contaminantes químicos, relaves y basura urbana. Su presencia o ausencia es el termómetro definitivo de la salud de nuestros ríos.

**Amenazas:** Hoy se encuentra en **En Peligro Crítico (CR)** debido a la severa contaminación de la cuenca del Río Chili y la pérdida de hábitat por el crecimiento urbano."""
    },
    "Vicuña": {
        "cientifico": "Vicugna vicugna",
        "imagen": "Vicugna_vicugna.png",
        "articulo": """La **Vicuña** es el camélido silvestre más pequeño del mundo y un símbolo vivo de la fauna peruana que adorna nuestro Escudo Nacional. Habita en las altiplanicies andinas expuestas a variaciones térmicas extremas.

**Características únicas:** Posee la fibra animal más fina y cotizada del planeta, una adaptación evolutiva que le proporciona una capa térmica impenetrable contra el frío de la puna. Sus pezuñas acolchadas no erosionan los frágiles suelos altoandinos y sus hábitos de pastoreo permiten que la vegetación nativa se regenere sin ser arrancada de raíz.

**Conservación:** Estuvo al borde de la extinción en los años 60 por la caza furtiva. Gracias a las reservas comunales y leyes estrictas, su estado actual es de **Preocupación Menor (LC)**, siendo un modelo exitoso de conservación comunitaria."""
    },
    "Puya Raimondi": {
        "cientifico": "Puya raimondii",
        "imagen": "La_Puya_Raimondi.png",
        "articulo": """Conocida como la "Titanca", la **Puya Raimondi** es la reina indiscutible de la flora de la puna. Es una planta gigante de la familia de las bromelias que tarda entre **80 y 100 años en alcanzar la madurez**.

**El gran florecimiento:** Al final de su larguísima vida, produce una inflorescencia colosal de hasta 10 metros de altura que alberga más de 8,000 flores y millones de semillas. Una vez que florece y dispersa sus semillas, la planta muere. Durante su florecimiento, se convierte en un centro biológico que atrae a decenas de especies de picaflores y aves andinas.

**Amenazas:** Está catalogada **En Peligro (EN)** debido al pastoreo descontrolado, ya que el ganado a veces queda atrapado en sus hojas espinosas, lo que lleva a algunos pastores a quemarlas erróneamente."""
    },
    "Corotilla": {
        "cientifico": "Cumulopuntia corotilla",
        "imagen": "Cumulopuntia corotilla.png",
        "articulo": """La **Corotilla** es un cactus nativo y endémico de las laderas áridas y desérticas de Arequipa. Crece formando densos cojines o agrupaciones de esferas globosas armadas con espinas amarillentas muy agudas.

**Héroe del desierto:** Cumple una función crucial en la física del suelo de los cerros arequipeños: sus raíces extendidas amarran la tierra suelta, evitando los deslizamientos en las pocas temporadas de lluvia, y actúan reteniendo la escasa humedad de las nieblas costeras que entran a los valles.

**Importancia educativa:** Es una planta ideal para biohuertos escolares xerofíticos debido a su nulo requerimiento de riego y su alto valor didáctico en adaptaciones morfológicas."""
    },
    "Guanaco": {
        "cientifico": "Lama guanicoe",
        "imagen": "Lama_guanicoe.png",
        "articulo": """El **Guanaco** es el camélido silvestre más grande de Sudamérica. A diferencia de la vicuña, el guanaco tiene una distribución más amplia y una fisionomía robusta con un característico rostro gris oscuro y pelaje marrón grueso.

**Ingeniero ecológico:** En las zonas áridas y lomas de Arequipa, los guanacos realizan largas migraciones estacionales buscando pastos frescos. Al consumir frutos y plantas secas, actúan como dispersores de semillas a través de sus excretas, ayudando a reforestar el desierto de manera natural.

**Amenazas:** Sus poblaciones en el Perú están drásticamente reducidas debido a la competencia por pastos con el ganado doméstico y la caza ilegal, por lo que está considerado **En Peligro (EN)** a nivel nacional."""
    },
    "Canastero de Arequipa": {
        "cientifico": "Asthenes arequipae",
        "imagen": "Asthenes arequipae.png",
        "articulo": """El **Canastero de Arequipa** es una pequeña y ágil ave passeriforme de plumaje pardo que habita en matorrales áridos y laderas con cactus de la región sudoccidental del Perú.

**Arquitecto de la naturaleza:** Su nombre proviene de la increíble forma en que construye sus nidos: grandes estructuras globosas hechas de ramitas entrelazadas que parecen "canastas" colgadas de los arbustos o cactus espinosos. Estos nidos protegen a sus crías tanto de los depredadores como de los cambios bruscos de temperatura. Su alimentación se basa en insectos, actuando como un excelente controlador biológico de plagas agrícolas."""
    },
    "Lombriz Californiana": {
        "cientifico": "Eisenia foetida",
        "imagen": "Eisenia_foetida.png",
        "articulo": """La **Lombriz Roja Californiana** es el motor biológico oculto de los proyectos sostenibles de reciclaje orgánico y biohuertos escolares.

        
        
**La alquimista del suelo:** Aunque es una especie introducida y criada globalmente, su importancia en la conservación escolar es insustituible. Devora desechos vegetales descompuestos y los transforma en **humus de lombriz**, el fertilizante orgánico más potente del mundo. Al excavar túneles constantemente, oxigena la tierra, permitiendo que las raíces de las plantas respiren y absorban agua eficientemente, combatiendo la compactación de los suelos escolares."""
    },
    "Malesherbia": {
        "cientifico": "Malesherbia angustisecta",
        "imagen": "Malesherbia_angustisecta.png",
        "articulo": """Conocida localmente como **Chavelina de cerro**, esta planta arbustiva es una joya botánica endémica que solo crece en las quebradas secas y pedregosas de los valles de Arequipa.

**Resistencia extrema:** Posee hojas profundamente recortadas cubiertas de pequeños pelos glandulares que secretan sustancias para defenderse de insectos herbívoros y reducir la evaporación. Sus flores tienen un diseño arquitectónico único adaptado a polinizadores especializados del desierto. Se encuentra clasificada **En Peligro (EN)** debido al crecimiento de proyectos mineros e inmobiliarios sobre sus reducidos hábitats nativos."""
    },
    "Tarasa": {
        "cientifico": "Tarasa marianii",
        "imagen": "Tarasa_marianii.png",
        "articulo": """La **Hierba Tarasa** es una planta herbácea silvestre nativa de la región que destaca por sus delicadas flores de tonos rosados, violáceos o púrpuras que aparecen con fuerza después de las lluvias veraniegas.

**Planta pionera:** Su gran valor ecológico radica en su capacidad para colonizar suelos degradados, erosionados o perturbados. Al fijarse en terrenos difíciles, sus raíces estabilizan el sustrato y preparan el terreno para que otras especies de plantas más demandantes puedan crecer en el futuro, liderando la sucesión ecológica natural."""
    },
        "Abutilon de Arequipa": {
        "cientifico": "Abutilon arequipense",
        "imagen": "Abutilon_arequipense.png",
        "articulo": """El Abutilon de Arequipa es un arbusto nativo que produce hermosas flores acampanadas de colores vivos y péndulas (que cuelgan hacia abajo).
Imán de picaflores: La forma de sus flores está perfectamente co-evolucionada con el pico de las aves polinizadoras locales, especialmente los picaflores andinos. Al buscar el néctar en el fondo de la campana, las aves se cubren la frente de polen y lo transportan a otros arbustos, asegurando la reproducción cruzada de la flora nativa en los ecosistemas de matorral de la región."""
    },
        "Cactus Gigantón": {
        "cientifico": "Neoraimondia arequipensis",
        "imagen": "Neoraimondia_arequipensis.png",
        "articulo": """El Cactus Gigantón es el coloso de los paisajes áridos de Arequipa. Este cactus columnar puede medir hasta 10 metros de altura y desarrollar múltiples brazos erguidos cubiertos de areolas con espinas formidables.
Planta nodriza: Funciona como un ecosistema en sí mismo. En su superficie anidan aves, sus flores nocturnas alimentan a murciélagos polinizadores y sus frutos jugosos son vitales para la fauna del desierto durante las sequías. Además, ofrece sombra en su base, actuando como "planta nodriza" que permite el nacimiento de plantas más débiles que morirían bajo el sol directo."""
    },
}
especie_seleccionada = st.sidebar.selectbox("🔎 Elige una especie:", ["Ninguna - Usar clave dicotómica"] + list(articulos_especies.keys()))
if especie_seleccionada != "Ninguna - Usar clave dicotómica":
    # Título con el nombre de la especie seleccionada
    st.sidebar.markdown(f"## 📌 {especie_seleccionada}")
    
    # Nombre científico extraído del diccionario
    st.sidebar.markdown(f"**Nombre Científico:** {articulos_especies[especie_seleccionada]['cientifico']}")
    
    # Texto o artículo descriptivo
    st.sidebar.write(articulos_especies[especie_seleccionada]["articulo"])
    
    # Intento de cargar la imagen correspondiente
    try:
        st.sidebar.image(
            articulos_especies[especie_seleccionada]["imagen"], 
            caption=f"{especie_seleccionada} - Vista del proyecto"
        )
    except Exception:
        st.sidebar.warning(f"⚠️ Imagen '{articulos_especies[especie_seleccionada]['imagen']}' no encontrada en el directorio.")
        
    # Línea divisoria al final de la sección
    st.sidebar.divider()
# Título principal de la aplicación
st.title("⛰️ Guía Taxonómica Digital de Arequipa")

# Subtítulo o enfoque del proyecto
st.markdown("### Conservación de Áreas Verdes Escolares y Biodiversidad Local")

# Descripción corta para el usuario
st.write("Usa esta clave dicotómica interactiva para identificar las 13 especies del proyecto tecnológico sostenible.")

# Línea divisoria para separar la introducción del contenido interactivo
st.divider()
# Encabezado de la sección interactiva
st.header("🔍 Identificador de Especies")

# Instrucción clara para el usuario
st.write("Responde las siguientes características observables para descartar e identificar tu especie:")
# Primera pregunta de la clave dicotómica para separar Reinos
reino = st.radio(
    "1. ¿Qué tipo de organismo general estás observando?",
    options=[
        "Selecciona una opción", 
        "Pertenece al Reino Plantae (Plantas, flores, cactus o árboles)", 
        "Pertenece al Reino Animalia (Mamíferos, aves, anfibios o anélidos)"
    ]
)
if "Reino Plantae" in reino:
    tipo_planta = st.radio(
        "2. ¿Cuál es su estructura física o forma de crecimiento principal?",
        options=[
            "Selecciona una opción", 
            "Es una planta suculenta (Cactus) con espinas prominentes", 
            "Es un árbol, arbusto o hierba con hojas o flores tradicionales"
        ]
    )
    
    if "Cactus" in tipo_planta:
        tipo_cactus = st.radio(
            "3. ¿Cómo es la forma de crecimiento de este cactus?",
            options=[
                "Selecciona una opción", 
                "Crece de forma esférica u ovoide, agrupado como pequeños cojines globosos", 
                "Crece de forma columnar, como un cactus gigante erecto de gran altura"
            ]
        )
        
        if "esférica" in tipo_cactus:
            st.success("¡Especie Identificada: Corotilla!")
            st.subheader("Cumulopuntia corotilla")
            st.image("Cumulopuntia corotilla.png", caption="Corotilla - Cactácea Nativa de Arequipa")
            st.markdown("Importancia Ecológica: Planta suculenta endémica clave para evitar la desertificación y retener agua en suelos áridos.")
            st.markdown("Estado de Conservación: No Evaluado (NE) / Preocupación Menor a nivel regional.")
            
        elif "columnar" in tipo_cactus:
            st.success("¡Especie Identificada: Cactus Gigantón!")
            st.subheader("Neoraimondia arequipensis")
            st.image("Neoraimondia_arequipensis.png", caption="Cactus Gigantón - Columna del desierto")
            st.markdown("Importancia Ecológica: Cactus columna central de interacciones ecológicas; sirve como planta nodriza y alimento en desiertos.")
            st.markdown("Estado de Conservación: Preocupación Menor (LC).")
        elif "árbol, arbusto" in tipo_planta:
            forma_planta = st.radio(
            "3. Elige la característica específica de sus hojas, flores o forma de vida:",
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
            st.subheader("Polylepis rugulosa")
            st.image("Polylepis_rugulosa.png", caption="Queñual - Bosques de Altura")
            st.markdown("Importancia Ecológica: Forma bosques de altura que regulan el agua y previenen la erosión de las laderas.")
            st.markdown("Estado de Conservación: Vulnerable (VU).")
            
        elif "cojín verde" in forma_planta:
            st.success("¡Especie Identificada: Yareta!")
            st.subheader("Azorella compacta")
            st.image("Azorella_compacte.png", caption="Yareta - Almohadilla Altoandina")
            st.markdown("Importancia Ecológica: Fijadora de carbono y protectora de suelos áridos altoandinos.")
            st.markdown("Estado de Conservación: Casi Amenazada (NT).")
            
        elif "planta gigante" in forma_planta:
            st.success("¡Especie Identificada: Puya Raimondi!")
            st.subheader("Puya raimondii")
            st.image("La_Puya_Raimondi.png", caption="Puya Raimondi - Titanca")
            st.markdown("Importancia Ecológica: Provee refugio y néctar a aves polinizadoras en hábitats extremos.")
            st.markdown("Estado de Conservación: En Peligro (EN).")
            
        elif "flores acampanadas" in forma_planta:
            st.success("¡Especie Identificada: Abutilon de Arequipa!")
            st.subheader("Abutilon arequipense")
            st.image("Abutilon_arequipense.png", caption="Abutilon de Arequipa - Arbusto endémico")
            st.markdown("Importancia Ecológica: Arbusto endémico cuyas flores acampanadas son clave para el alimento de picaflores locales.")
            st.markdown("Estado de Conservación: No Evaluado (NE).")
            
        elif "Chavelina" in forma_planta:
            st.success("¡Especie Identificada: Malesherbia / Chavelina!")
            st.subheader("Malesherbia angustisecta")
            st.image("Malesherbia_angustisecta.png", caption="Malesherbia angustisecta - Flora endémica")
            st.markdown("Importancia Ecológica: Planta endémica adaptada a la aridez, vital para la diversidad florística local.")
            st.markdown("Estado de Conservación: En Peligro (EN).")
            
        elif "Hierba Tarasa" in forma_planta:
            st.success("¡Especie Identificada: Tarasa!")
            st.subheader("Tarasa marianii")
            st.image("Tarasa_marianii.png", caption="Tarasa marianii - Flora nativa")
            st.markdown("Importancia Ecológica: Especie pionera que ayuda a la recuperación de suelos degradados.")
            st.markdown("Estado de Conservación: No Evaluado (NE).")
elif "Reino Animalia" in reino:
    tipo_animal = st.radio(
        "2. ¿Qué estructura anatómica o hábitat principal presenta el animal?",
        options=[
            "Selecciona una opción", 
            "Vertebrado terrestre con patas (Mamífero o Ave)", 
            "Anfibio acuático o Invertebrado alargado sin patas"
        ]
    )
    
    if "Vertebrado terrestre" in tipo_animal:
        forma_animal = st.radio(
            "3. Identifícalo por su grupo o pelaje/plumaje:",
            options=[
                "Selecciona una opción",
                "Es un ave pequeña y ágil de plumaje pardo, conocida como 'Canastero de Arequipa'",
                "Es un camélido silvestre de pelaje fino y color canela dorado, emblemático nacional",
                "Es un camélido silvestre de mayor tamaño, hocico oscuro y pelaje marrón más grueso"
            ]
        )
        
        if "ave pequeña" in forma_animal:
            st.success("¡Especie Identificada: Canastero de Arequipa!")
            st.subheader("Asthenes arequipae")
            st.image("Asthenes arequipae.png", caption="Canastero de Arequipa")
            st.markdown("Importancia Ecológica: Ave endémica que actúa como controladora de insectos en ecosistemas áridos.")
            st.markdown("Estado de Conservación: Preocupación Menor (LC).")
            
        elif "pelaje fino" in forma_animal:
            st.success("¡Especie Identificada: Vicuña!")
            st.subheader("Vicugna vicugna")
            st.image("Vicugna_vicugna.png", caption="Vicuña - Símbolo de la Fauna Peruana")
            st.markdown("Importancia Ecológica: Especie paraguas clave en el pastoreo estacional y la cadena trófica de la puna.")
            st.markdown("Estado de Conservación: Preocupación Menor (LC).")
            
        elif "mayor tamaño" in forma_animal:
            st.success("¡Especie Identificada: Guanaco!")
            st.subheader("Lama guanicoe")
            st.image("Lama_guanicoe.png", caption="Guanaco - Camélido Silvestre")
            st.markdown("Importancia Ecológica: Herbívoro nativo que dispersa semillas y mantiene el equilibrio de los pastizales.")
            st.markdown("Estado de Conservación: Preocupación Menor (LC) a nivel global.")
            
    elif "Anfibio acuático" in tipo_animal:
        forma_bajo_agua = st.radio(
            "3. Observa su cuerpo y su entorno:",
            options=[
                "Selecciona una opción",
                "Es un anfibio de piel húmeda que vive oculto en ríos y arroyos de la región",
                "Es un organismo anélido (gusano), alargado, blando, segmentado y vive bajo la tierra húmeda"
            ]
        )
        
        if "anfibio" in forma_bajo_agua:
            st.success("¡Especie Identificada: Rana de Arequipa!")
            st.subheader("Telmatobius arequipensis")
            st.image("Telmatobius_arequipensis.png", caption="Rana acuática de Arequipa")
            st.markdown("Importancia Ecológica: Indicadora clave de la salud y pureza de los ecosistemas acuáticos.")
            st.markdown("Estado de Conservación: En Peligro Crítico (CR).")
            
        elif "organismo anélido" in forma_bajo_agua:
            st.success("¡Especie Identificada: Lombriz Roja Californiana!")
            st.subheader("Eisenia foetida")
            st.image("Eisenia_foetida.png", caption="Lombriz Roja - Aliada del compostaje")
            st.markdown("Importancia Ecológica: Descomponedora clave que enriquece el suelo mediante el vermicompostaje escolar.")
            st.markdown("Estado de Conservación: No evaluada comercialmente / Altamente beneficiosa.")
st.divider()
st.header("📊 Documentación Científica")

with st.expander("📋 Hacer clic para ver la Tabla Taxonómica Completa"):
    st.write("Este registro contiene la jerarquía científica exacta de las 13 especies seleccionadas para la ficha del proyecto:")
    
    # Diccionario de datos taxonómicos estructurado
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
    # Renderizar la tabla interactiva usando la función nativa de Streamlit
    st.dataframe(datos_completos, use_container_width=True)
# Checkbox interactivo para mostrar u ocultar la tabla de datos
mostrar_tabla = st.checkbox("¿Deseas ver la tabla de datos completa?", value=True)
if mostrar_tabla:
    # Despliega la tabla interactiva si el checkbox está marcado
    st.dataframe(datos_completos, use_container_width=True)
# --- SECCIÓN 3: GRÁFICO DINÁMICO DE PRESENCIA POR ESPECIE ---
st.divider()
st.header("🗺️ Distribución Geográfica en Arequipa")
st.write("Selecciona una especie para ver en qué provincias de la región Arequipa se encuentra su mayor presencia o hábitat principal:")

# Base de datos de presencia (en escala de 0 a 10 de abundancia/probabilidad) por provincia para las 13 especies
datos_distribucion_especies = {
    "Yareta": {
        "Provincias": ["Caylloma", "La Unión", "Castilla", "Condesuyos", "Arequipa (Alturas)"],
        "Nivel de Presencia": [10, 8, 7, 6, 5]
    },
    "Queñual": {
        "Provincias": ["Caylloma", "Arequipa (Chiguata/Pichu Pichu)", "La Unión", "Castilla", "Condesuyos"],
        "Nivel de Presencia": [10, 9, 8, 6, 5]
    },
    "Rana de Arequipa": {
        "Provincias": ["Arequipa (Río Chili)", "Caylloma", "Castilla", "Condesuyos"],
        "Nivel de Presencia": [10, 7, 5, 4]
    },
    "Vicuña": {
        "Provincias": ["Caylloma (Salinas y Aguada Blanca)", "Arequipa", "Castilla", "La Unión", "Condesuyos"],
        "Nivel de Presencia": [10, 8, 7, 7, 6]
    },
    "Puya Raimondi": {
        "Provincias": ["Caylloma", "La Unión", "Castilla", "Caravelí (Alturas)"],
        "Nivel de Presencia": [10, 9, 6, 4]
    },
    "Corotilla": {
        "Provincias": ["Arequipa (Cerros locales)", "Caylloma", "Castilla", "Condesuyos"],
        "Nivel de Presencia": [10, 6, 5, 4]
    },
    "Guanaco": {
        "Provincias": ["Caravelí", "Castilla", "Condesuyos", "Arequipa"],
        "Nivel de Presencia": [10, 7, 6, 4]
    },
    "Canastero de Arequipa": {
        "Provincias": ["Arequipa", "Caylloma", "Castilla", "La Unión", "Caravelí"],
        "Nivel de Presencia": [10, 8, 7, 6, 5]
    },
    "Lombriz Californiana": {
        "Provincias": ["Arequipa (Biohuertos urbanos)", "Camaná (Zonas agrícolas)", "Islay (Zonas agrícolas)", "Caylloma (Majes)"],
        "Nivel de Presencia": [10, 8, 8, 7]
    },
    "Malesherbia": {
        "Provincias": ["Arequipa (Quebradas dry)", "Castilla", "Condesuyos", "Caravelí"],
        "Nivel de Presencia": [10, 7, 6, 5]
    },
    "Tarasa": {
        "Provincias": ["Arequipa", "Caylloma", "Castilla", "La Unión", "Condesuyos"],
        "Nivel de Presencia": [9, 9, 7, 6, 6]
    },
    "Abutilon de Arequipa": {
        "Provincias": ["Arequipa (Matorrales)", "Caylloma", "Castilla"],
        "Nivel de Presencia": [10, 7, 5]
    },
    "Cactus Gigantón": {
        "Provincias": ["Arequipa (Yura/Chiguata)", "Caravelí", "Castilla", "Condesuyos"],
        "Nivel de Presencia": [10, 9, 7, 6]
    }
}

# Selector interactivo para el gráfico
especie_grafico = st.selectbox(
    "📊 Elige una especie para generar su gráfico de ubicación:", 
    list(datos_distribucion_especies.keys())
)

# Extraer los datos de la especie seleccionada
provincias_lista = datos_distribucion_especies[especie_grafico]["Provincias"]
presencia_lista = datos_distribucion_especies[especie_grafico]["Nivel de Presencia"]

# Crear el gráfico dinámico con Plotly
figura_dinamica = px.bar(
    x=presencia_lista,
    y=provincias_lista,
    orientation="h",
    title=f"Nivel de Presencia Estimado de la Especie: {especie_grafico}",
    labels={"x": "Índice de Presencia / Abundancia (0 al 10)", "y": "Provincias de Arequipa"},
    color=presencia_lista,
    color_continuous_scale="Cividis"
)

# Ordenar las barras para que la provincia con más presencia salga arriba
figura_dinamica.update_layout(yaxis={'categoryorder': 'total ascending'}, height=350)

# Mostrar el gráfico en Streamlit
st.plotly_chart(figura_dinamica, use_container_width=True)





