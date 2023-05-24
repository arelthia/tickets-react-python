import { ReactElement } from "react";

type HeadingProps = { title: string };

const Heading = ({ title }: HeadingProps): ReactElement => {
  return (
    <header className="branding">
      <h1 className="site-title">{title}</h1>
    </header>
  )
}

export default Heading;