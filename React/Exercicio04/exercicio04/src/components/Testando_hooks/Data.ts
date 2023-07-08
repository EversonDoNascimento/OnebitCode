import { useState } from "react";

export const Data = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const setData = (email: string, password: string) => {
    setEmail(email);
    setPassword(password);
  };
};
