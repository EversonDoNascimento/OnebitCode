import { GetServerSideProps, GetStaticProps, NextPage } from "next";
import { useEffect, useState } from "react";
import { Container, Row, Col } from "reactstrap";
import { ReactNode } from "react";
interface ApiResponse {
  name: string;
  timestamp: Date;
}
interface StaticProps {
  staticData?: ApiResponse;
}
export const getStaticProps: GetStaticProps = async () => {
  const staticData = await fetch(
    `${process.env.NEXT_PUBLIC_APIURL}/api/hello`
  ).then((res) => res.json());
  return {
    props: {
      staticData,
    },
    revalidate: 10,
  };
};

const Static: NextPage = (props: {
  children?: ReactNode;
  staticData?: ApiResponse;
}) => {
  const [clientSideData, setClientSideData] = useState<ApiResponse>();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const data = await fetch("/api/hello").then((res) => res.json());
    setClientSideData(data);
  };
  return (
    <Container>
      <h1 className="my-5">Como funcionam as renderizações no Next.js</h1>
      <Row>
        <Col>
          <h3>Gerado</h3>
          <h2>{props.staticData?.timestamp.toString()}</h2>
        </Col>
        <Col>
          <h3>Gerado no cliente:</h3>

          <h2>{clientSideData?.timestamp.toString()}</h2>
        </Col>
      </Row>
    </Container>
  );
};

export default Static;
