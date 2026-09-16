# Taller Atracción Digital · Guía del instructor

Guía para dar las cuatro clases del taller (HERNANDEZ Academia): el embudo y el perfil, yapping, antes y después, asesoría y certificación. El entregable es `guia-instructor-atraccion-digital.pdf`.

- `contenido/` es el texto de la guía en Markdown, un archivo por clase más los anexos. Se edita ahí.
- `plantilla/` arma el HTML y el PDF (`estilos.css`, `build.mjs`) y saca vistas previas por página (`previews.py`).
- `assets/` tiene el logo del taller y las fuentes (Anton para títulos, Poppins para el cuerpo).

Para regenerar el PDF después de editar el contenido:

```
npm install
node plantilla/build.mjs
python3 plantilla/previews.py --hoja     # opcional, PNG por página en .previews/
```

Cada diapositiva se escribe como `## Diapositiva N. Título · X min`; los minutos se suman solos en la portada de cada clase.
