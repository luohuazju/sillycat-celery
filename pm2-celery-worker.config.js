module.exports = {
  apps: [
    {
      name: "celery-worker",
      script: "/Users/carl/.pyenv/shims/celery",
      args: "-A celery_task_ai worker --loglevel=DEBUG",
      exec_mode: "fork", // Use "cluster" if you want multiple instances
      instances: 4,      // Number of instances to run
      interpreter: "none",
      cwd: "/Users/carl/work/sillycat/sillycat-celery"
      autorestart: false, // Automatically restart if the process crashes
      watch: false,      // Set true to enable file watching
    },
  ],
};
