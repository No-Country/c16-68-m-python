import React, { Fragment, useState } from "react";

const ToDoList = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");

  const handleAddTodo = () => {
    if (newTodo.trim() !== "") {
      setTodos([...todos, { text: newTodo.trim(), checked: false }]);
      setNewTodo("");
    }
  };

  const handleDeleteTodo = (index) => {
    const newTodos = [...todos];
    <div class="modal-dialog modal-dialog-centered"></div>;
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  const handleToggleTodo = (index) => {
    const newTodos = [...todos];
    newTodos[index].checked = !newTodos[index].checked;
    setTodos(newTodos);
  };
  return (
    <div class="">
      <div className="container-sm">
        <h1>Mis Habitos Saludables</h1>
      </div>

      <div className="list-group">
        <div className="list-group-item">
          <input
            className="form-control m-0 p-3"
            type="text"
            value={newTodo}
            placeholder="Ingresa un nuevo habito saludable."
            onChange={(evento) => setNewTodo(evento.target.value)}
          />
          <div class="container pt-2  ">
            <button class="btn btn-primary pt-2" onClick={handleAddTodo}>
              Agregar Habito
            </button>
          </div>
        </div>
      </div>

      <div class="">
        <div class="list-group">
          <ul class="list-group-item">
            {todos.map((todo, index) => (
              <>
                <li class="" key={index} style={{ display: "flex" }}>
                  <div>
                    <div class="">
                      <div class="col form-check">
                        <input
                          class="form-check-input"
                          type="checkbox"
                          checked={todo.checked}
                          onChange={() => {
                            handleToggleTodo(index);
                          }}
                        ></input>
                      </div>
                    </div>
                    <div class="col">
                      <span
                        style={{
                          marginRight: "10px",
                          textDecoration: todo.checked
                            ? "line-through"
                            : "none",
                        }}
                      >
                        {todo.text}
                      </span>
                    </div>
                    <div class="">
                      <div class="col">
                        <button
                          class="btn btn-danger"
                          onClick={() => {
                            handleDeleteTodo(index);
                          }}
                        >
                          Eliminar
                        </button>
                      </div>
                    </div>
                  </div>
                </li>{" "}
              </>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default ToDoList;
