import { Generate } from "./Generate_Password/Generate";
import { ChakraBaseProvider, Heading, Container } from "@chakra-ui/react";
import theme from "./Theme/Theme";

import { Content } from "./Components/Content";

function App() {
  return (
    <>
      <ChakraBaseProvider theme={theme}>
        <Content></Content>
      </ChakraBaseProvider>
    </>
  );
}

export default App;
