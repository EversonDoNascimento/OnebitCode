import * as C from "./StyleProfile";
import DefaultProfile from "./../Images/User.png";
import { Button } from "./Button/Button";
import Github from "./../Images/github.svg";
import Linkedin from "./../Images/linkedin.svg";
import Twitter from "./../Images/twitter.svg";
type Props = {
  avatar: string;
  name: string;
  bio: string;
  email: string;
  phone: string;
  githubUrl: string;
  linkedinUrl: string;
  twitterUrl: string;
};
export const Profile = ({
  avatar,
  name,
  bio,
  email,
  phone,
  githubUrl,
  linkedinUrl,
  twitterUrl,
}: Props) => {
  return (
    <>
      <C.Container>
        <C.Content>
          <C.Avatar>
            <C.Imagem
              src={avatar ? avatar : DefaultProfile}
              alt={name ? "Foto do perfil de " + name : "Sem foto de perfil"}
            ></C.Imagem>

            <C.NameProfile>{name ? name : "Sem informações"}</C.NameProfile>
          </C.Avatar>
          <C.Line></C.Line>
          <C.Information>{bio ? bio : "Sem informações"}</C.Information>
          <C.Line></C.Line>
          <C.Information>{email ? email : "Sem informações"}</C.Information>
          <C.Line></C.Line>
          <C.Information>{phone ? phone : "Sem informações"}</C.Information>
          <C.Line></C.Line>
          <Button
            icon={Github}
            cor="#000"
            link={githubUrl}
            content="Github"
          ></Button>
          <Button
            icon={Linkedin}
            cor="#0961B8"
            link={linkedinUrl}
            content="LinkedIn"
          ></Button>
          <Button
            icon={Twitter}
            cor="#1D9BF0"
            link={twitterUrl}
            content="Twitter"
          ></Button>
        </C.Content>
      </C.Container>
    </>
  );
};
