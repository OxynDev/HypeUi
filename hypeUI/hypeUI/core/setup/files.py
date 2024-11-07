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

/* :root {
    height: 100%;
}

#root, body, #root > div {
    height: 100% !important;
}
 */
'''

css_app = '''#root {
  margin: 0 auto;
}
'''

main_jsx = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import { NextUIProvider } from '@nextui-org/react';
import {ThemeProvider as NextThemesProvider} from "next-themes";
import App from './App';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));

function renderApp(theme) {
  root.render(
    <React.StrictMode>
      <NextUIProvider>
        <NextThemesProvider attribute="class" defaultTheme={theme}>
          <App />
        </NextThemesProvider>
      </NextUIProvider>
    </React.StrictMode>
  );
}


window.setTheme = (themeType) => {
  renderApp(themeType === 'dark' ? 'dark' : 'light');
};
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
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
'''