import React from 'react';

type Props = {
  data: any[];
};

const Graph: React.FC<Props> = ({ data }) => {
  return (
    <div>
      <h2>Stock Price Visualization</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default Graph;
