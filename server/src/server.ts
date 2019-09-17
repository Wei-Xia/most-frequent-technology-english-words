import { settings } from './config/config';
import express from 'express';
import { ApolloServer } from 'apollo-server-express';
import { typeDefs } from './typeDefs';
import { resolvers } from './resolvers/resolvers';
import { mongoose, handleError } from 'mongoose';

const startServer = async () => {
  const server = new ApolloServer({ typeDefs, resolvers });

  const app = express();
  server.applyMiddleware({ app });
  console.log(settings.mongoDB);
  await mongoose
    .connect(settings.mongoDB, {
      useNewUrlParser: true,
    })
    .catch((error) => handleError(error));

  app.listen({ port: 4000 }, () =>
    console.log(
      `🚀 Server ready at http://localhost:4000${server.graphqlPath}`,
    ),
  );
};

startServer();
