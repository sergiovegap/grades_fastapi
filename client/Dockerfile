FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

# install with --production (exclude devDependencies)
# RUN mkdir -p /temp/prod

# [optional] tests & build
# ENV NODE_ENV=production
# RUN npm test
# RUN npm run build

EXPOSE 5173

CMD [ "npm", "run", "dev" ]
