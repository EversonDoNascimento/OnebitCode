import { Test } from "./assets/Test";
import { TextCard } from "./Components/TextCard/TextCard";
import Image from "./image.jpg";
import Image2 from "./assets/image2.jpg";
function App() {
  return (
    <>
      <TextCard poster={Image} title={"Pôster: Star Wars (1977)"}></TextCard>
      <TextCard
        poster={Image2}
        title={"Pôster: Empire Strikes Back (1980)"}
      ></TextCard>
      <TextCard poster={Image} title={"Pôster: Star Wars (1999)"}></TextCard>
    </>
  );
}

export default App;
