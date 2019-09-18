import express from 'express';
import { ApolloServer } from 'apollo-server-express';
import mongoose from 'mongoose';
import { settings } from './utils/config';
import { typeDefs } from './typeDefs';
import { resolvers } from './resolvers/resolvers';

const startServer = async () => {
  const server = new ApolloServer({ typeDefs, resolvers });

  const app = express();
  server.applyMiddleware({ app });
  await mongoose
    .connect(settings.mongodbURL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
    .catch((error) => {
      console.log(error);
    });

  app.listen({ port: 4000 }, () => console.log(
    `🚀 Server ready at http://localhost:4000${server.graphqlPath}`,
  ));
};

startServer();
