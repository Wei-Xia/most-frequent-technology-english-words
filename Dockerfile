FROM ruby:3.2-slim

WORKDIR /app

# 安装依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    nodejs \
    npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装 Ruby 依赖
COPY Gemfile Gemfile.lock* ./
RUN bundle install

# 安装 Node.js 依赖（如果需要）
COPY package.json package-lock.json* ./
RUN npm install

# 复制项目文件
COPY . .

# 暴露端口
EXPOSE 4000

# 启动命令
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--livereload"]