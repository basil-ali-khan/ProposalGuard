FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# NEXT_PUBLIC_API_URL must be set as a Space secret — it's baked in at build time
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL

RUN npm run build

EXPOSE 7860
ENV PORT=7860
ENV HOSTNAME=0.0.0.0

CMD ["npm", "start"]
