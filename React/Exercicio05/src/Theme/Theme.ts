import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  colors: {
    primary: "#FF0000",
    secondary: "#00FF00",
  },
  styles: {
    global: {
      body: {
        bg: "#2e2e2e", // Defina a cor desejada para o fundo da página
      },
    },
  },
});

export default theme;
