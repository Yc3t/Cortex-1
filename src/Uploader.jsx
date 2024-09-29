import React, { useState } from "react";
import axios from "axios";

const Uploader = () => {
  const [file, setFile] = useState();

  //handle the change of the state

  function handleChange(event) {
    //show the file
    setFile(event.target.files[0]);
  }

  function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const url = "http://localhost:5000/uploadFile";
    const formData = new FormData();
    formData.append("file", file);
    formData.append("fileName", file.name);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };

    axios.post(url, formData, config).then((response) => {
      console.log(response.data);
    });
  }

  return (
    <>
      <form onSubmit={handleSubmit} className="flex flex-col">
        <input type="file" onChange={handleChange} />
        <button className="mt-4" type="submit">
          send
        </button>
      </form>
    </>
  );
};

export default Uploader;

