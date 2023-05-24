import { ReactElement, ReactNode } from 'react';

type MainProps = {
    children: ReactNode
}

const Main = ({children}: MainProps): ReactElement => {
  return (
    <main>
        {children}
    </main>
  )
}

export default Main;