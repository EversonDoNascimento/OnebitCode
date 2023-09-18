import * as C from "./StyleButton";
type Props = {
  cor: string;
  link: string;
  content: string;
  icon: string;
};
export const Button = ({ cor, link, content, icon }: Props) => {
  return (
    <>
      <C.Button style={{ backgroundColor: cor, border: "none" }}>
        <C.Center>
          <C.Icon src={icon}></C.Icon>

          <C.Link href={link} target="_blank">
            {content}
          </C.Link>
        </C.Center>
      </C.Button>
    </>
  );
};
