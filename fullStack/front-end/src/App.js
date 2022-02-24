import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {Input, Form, Button, Container} from 'react-bootstrap'

import {useState, useEffect, useReducer} from 'react';


function reducer(state, action){
  console.log("arrived in reducer method!");
  console.log("state at reducer is: ",state);

  switch(action.name){
    case "fileName":
      return {...state, fileName : action.data.fileName}
    case "foundFiles":
      return {...state, files: action.data.files }
  }
    return state
}

function App() {
  const [name, setName] = useState("ayon!");
  const [number, setNumber] = useState(0);
  const [selectedFile, setSelectedFile] = useState(null);
  const [state, dispatch] = useReducer(reducer, {files : [], fileName : ""})
  console.log("state at first render is: ",state);
  var fileBlock = []
  var myDictionary = {"name" : "ayon", "age" : 30}
  for (let key in myDictionary) {
    let value = myDictionary[key];
    // Use `key` and `value`
    console.log(`key value is ${key} and value is ${value}`)
}
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

  // const object = {'a': 1, 'b': 2, 'c' : 3};

  // for (const [key, value] of Object.entries(object)) {
  //   console.log(key, value);
  // }

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
    console.log("state in searchFile method is: ",state)
    try{
      const matchedFiles = await axios({
        method: "POST",
        url: "http://127.0.0.1:5000/search-files",
        data: state
      });
      console.log("files from search files are: ", matchedFiles);
      dispatch({ name: "foundFiles", data: { files: matchedFiles} })
    }
    catch (error){
      console.error(error);
    }
      console.log("state after saving searched files: ",state)
  }


  function handleInput(e){
    dispatch({ name: "fileName", data: { fileName : e.target.value } })
  }

  if(state.files.data != undefined){
    for ( let key in state.files.data ){
      console.log("state.files.data is: ",state.files.data)
      console.log("current key value pair is: ",key, state.files.data[key]);
      fileBlock.push(<li><div> {key} : {state.files.data[key]} </div></li>)
    }
    var allFilesBlock = <ul>{fileBlock}</ul>;
    dispatch({ name: "foundFiles", data : { files: allFilesBlock } })
  }
  console.log("state before rendering is: ",state)
  return (
    <div className="App">
      {/* hello world!
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
      The number you have entered is: {number} */}
      <br></br>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileUpload}></input>
        <button>Upload</button>
      </form>
      <br></br>
      <button onClick={createBucket}>Create bucket</button>
      <br></br>
      <br></br>
      <form onSubmit={searchFile}>
        <input value={state.fileName} name="fileName" onChange={(e) => handleInput(e)}></input>
        <button>Search file</button>
      </form>
      {state.files}
    </div>
  );
}

export default App;
