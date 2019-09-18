import { gql } from 'apollo-server-express';

export const typeDefs = gql`
  type Query {
    words: [wordList!]!
  }
  type wordList {
    id: ID!
    name: String!
  }
  type Mutation {
    createNewWord(name: String!): wordList!
  }
`;
