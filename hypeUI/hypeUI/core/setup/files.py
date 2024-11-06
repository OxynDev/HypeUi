tailwind_config =  '''const { nextui } = require("@nextui-org/react");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // ...
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {},
  },
  darkMode: "class",
  plugins: [nextui()]
}'''


css = '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
    height: 100%;
}

#root, body, #root > div {
    height: 100% !important;
}

'''

main_jsx = '''import React from 'react'
import ReactDOM from 'react-dom/client'
import {NextUIProvider} from '@nextui-org/react'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <NextUIProvider>
      <App />
    </NextUIProvider>
  </React.StrictMode>,
)
'''

app_jsx = '''import { useState } from 'react'
import './App.css'
// ||IMPORT||

function App() {
  const [count, setCount] = useState(0)
  // ||CONTENT||
  return (
    <>
      {/* ||RETURN|| */}
    </>
  )
}

export default App

'''

html = '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>HypeUi</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
'''