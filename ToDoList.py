import streamlit as st

class ToDoList:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        self.tareas.append({"descripcion": descripcion, "completada": False}) 

    def marcar_completada(self, indice): 
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)

    def obtener_tareas(self):
        return self.tareas



st.title(" - - - To-Do List  - - -")

if "todo" not in st.session_state:
    st.session_state.todo = ToDoList()

st.subheader("Agregar nueva tarea")
nueva_tarea = st.text_input("Descripción de la tarea")

if st.button("Agregar"):
    if nueva_tarea:
        st.session_state.todo.agregar_tarea(nueva_tarea)
        st.success("Tarea agregada correctamente.")
    else:
        st.warning("Escriba una tarea primero.")

st.subheader("Tareas pendientes")
tareas = st.session_state.todo.obtener_tareas()

if not tareas:
    st.info("No hay tareas pendientes.")
else:
    for i, tarea in enumerate(tareas):
        cols = st.columns([0.05, 0.8, 0.15])
        if not tarea["completada"]:
            if cols[0].checkbox("", key=f"check_{i}"):
                st.session_state.todo.marcar_completada(i)
        cols[1].write(f"**{tarea['descripcion']}**" if not tarea["completada"] else f"✅ ~~{tarea['descripcion']}~~")
        if cols[2].button("Borrar", key=f"del_{i}"):
            st.session_state.todo.eliminar_tarea(i)
            st.rerun()
