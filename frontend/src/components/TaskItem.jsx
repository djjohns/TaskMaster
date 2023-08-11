/* eslint-disable react/prop-types */
export function TaskItem({ complete, task_id, title, toggleTask, deleteTask }) {
    return (
      <li>
        <label>
          <input
            type="checkbox"
            checked={complete}
            onChange={e => toggleTask(task_id, e.target.checked)}
          />
          {/* {task_id} */}
          {title}
        </label>
        <button onClick={() => deleteTask(task_id)} className="btn btn-danger">
          Delete
        </button>
      </li>
    )
  }