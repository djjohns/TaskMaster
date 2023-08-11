import { useEffect, useState } from "react"
import { NewTaskForm } from "./components/NewTaskForm"
import { TaskList } from "./components/TaskList"
import TopNavbar from "./components/TopNavbar";
import axios from 'axios';
import "./styles.css"



export default function App() {
  const [tasks, setTasks] = useState([]);

  async function fetchData() {
    try {
      console.log('Fetching data...');
      const response = await axios.get('http://localhost:8000/api/task');
      console.log('Response:', response.data);
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  }

  useEffect(() => {fetchData();}, []);


  const refreshData = () => {
    fetchData();
  };


  function addTask(title) {
    axios.post("http://localhost:8000/api/task", {
      task_id: crypto.randomUUID(),
      title,
      complete: false
    }, {
      headers: {
        "Content-Type": "application/json",
      }
    })
    .then((response) => response.data)
    .then((newTask) => setTasks((prevTasks) => [...prevTasks, newTask]))
    .catch((error) => console.error("Error adding task:", error));
  }

  const toggleTask = async (task_id, complete) => {
    try {
      const response = await axios.put(`http://localhost:8000/api/task/${task_id}?complete=${complete}`);
      const updatedTask = response.data;
      refreshData();
      setTasks(prevTasks =>
        prevTasks.map(task => (task.task_id === updatedTask.task_id ? updatedTask : task))
      )
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };
  
  function deleteTask(task_id) {
    axios.delete(`http://localhost:8000/api/task/${task_id}`)
      .then(() => setTasks((prevTasks) => prevTasks.filter((task) => task.task_id !== task_id)))
      .catch((error) => console.error("Error deleting task:", error));
  }

  return (
    <>
      < TopNavbar />
      <br />
      <NewTaskForm onSubmit={addTask} />
      <h1 className="header">Task List</h1>
      <TaskList tasks={tasks} toggleTask={toggleTask} deleteTask={deleteTask} />
    </>
  );
}