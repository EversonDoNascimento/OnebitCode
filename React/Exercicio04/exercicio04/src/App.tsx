//import { Profile } from "./components/Profile";
//import ProfileUser from "./Images/profileUser.jpg";
import { useState } from "react";
import { Teste } from "./components/teste/teste";
import "./style.css";
import { ChakraProvider } from "@chakra-ui/react";
import theme from "./components/Theme"; // Importe o tema personalizado
import { Parent } from "./components/TestePai/Parent";
import { Children } from "./components/TestePai/Children";
import Login from "./components/testebutton/Login";
import { TesteData } from "./components/Testando_hooks/TesteData";
function App() {
  const [positionButton, setPositionButton] = useState();
  return (
    <>
      {/*
      <Profile
        name={"Everson Nascimento"}
        bio={"Engenheiro de Software - UX/UI"}
        githubUrl={"www.github.com"}
        linkedinUrl={"www.linkedin.com"}
        twitterUrl={"www.twitter.com"}
        email={"everson@gmail.com"}
        phone={"+55 (81) 9 5879-6587"}
        avatar={ProfileUser}
  ></Profile>*/}
      <ChakraProvider theme={theme}>
        <TesteData></TesteData>
      </ChakraProvider>
    </>
  );
}

export default App;
