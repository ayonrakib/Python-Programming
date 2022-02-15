import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {Input, Form, Button, Container} from 'react-bootstrap'

import {useState, useEffect, useReducer} from 'react';


function reducer(state, action){
  console.log("arrived in reducer method!");
  console.log("state at first is: ",state);

  switch(action.name){
    case "fileName":
      return {...state, value : action.data.value}
  }
    return state
}

function App() {
  const [name, setName] = useState("ayon!");
  const [number, setNumber] = useState(0);
  const [selectedFile, setSelectedFile] = useState(null);
  const [state, dispatch] = useReducer(reducer, {files : [], value : ""})

  useEffect(() => {
    axios({
      method: "GET",
      data: "",
      url: "http://127.0.0.1:5000/"
    }).then(response => {
      console.log("response from server is: ",response)
      setName(response.data)
    })
  },[])


  function getSquare(e){
    e.preventDefault();
    axios({
      method:"POST",
      data: {
        number: 9
      },
      url: "http://127.0.0.1:5000/get-square-of-number"
    }).then(response => {
      console.log("resposne from POST req is: ",response.data)
      setNumber(response.data)
    })
  }


  function handleFileUpload(event){
    setSelectedFile(event.target.files[0])
  }

  async function handleSubmit(event){
    event.preventDefault();
    console.log("file: ",selectedFile)

    
    const formData = new FormData();
    formData.append("selectedFile", selectedFile);
    console.log("form data is: ",formData)
    try {
      const response = await axios({
        method: "post",
        url: "http://127.0.0.1:5000/upload-file-in-s3",
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
      });
      console.log("response from upload-file-in-s3: ",response.data)
    } catch(error) {
      console.log(error)
    }
  }


  async function createBucket(event){
    event.preventDefault();
    try {
      const response = await axios({
        method: "GET",
        data: "",
        url: "http://127.0.0.1:5000/create-bucket"
      });
      console.log("response from create bucket url is: ",response.data)
    } catch (error) {
      console.error(error)
    }
  }


  async function searchFile(event){
    event.preventDefault();
    try{
      const files = await axios({
        method: "POST",
        url: "http://127.0.0.1:5000/search-files"
      });
      console.log("files from search files are: ", files);
    }
    catch (error){
      console.error(error);
    }
  }


  function handleInput(e){
    dispatch({ name: "fileName", data: { value : e.target.value } })
  }

  return (
    <div className="App">
      hello world!
      <br></br>
      {name}
      <Container>
        <Form>
          <Form.Group className="mb-3" controlId="number">
            <Form.Label>Enter number:</Form.Label>
            <Form.Control type="text" placeholder="Enter number" />
          </Form.Group>
          <Button variant="primary" type="submit" onSubmit={(e) => handleSubmit(e)}>
            Submit
          </Button>
        </Form>
      </Container>
      The number you have entered is: {number}
      <br></br>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileUpload}></input>
        <button>Upload</button>
      </form>
      <button onClick={createBucket}>Create bucket</button>
      <form onSubmit={searchFile}>
        <input value={state} name="fileName" onChange={(e) => handleInput(e)}></input>
        <button>Search file</button>
      </form>
    </div>
  );
}

export default App;
