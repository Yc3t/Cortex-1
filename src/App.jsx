import { useState } from 'react'
import Uploader from './Uploader'

function App() {

  return (
    <>
      <h1 className='text-center text-6xl mt-10'>Cortex 1 </h1>

        <div className='flex flex-col justify-center items-center '>
          
          <p> Handle Upload</p>
          <Uploader />      
       </div>


    </>
  )
}

export default App
