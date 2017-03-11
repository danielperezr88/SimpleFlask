FROM sdhibit/rpi-raspbian

RUN apt-get update && apt-get install -y \
	python-dev \
	python-pip \
	git \
	curl \
	supervisor

RUN pip install --upgrade pip && \
	pip install Flask && \
	pip install supervisor && \
	pip install superlance==1.0.0 && \
	pip install wiringpi

RUN curl -fSL "https://github.com/danielperezr88/SimpleFlask/archive/v1.0.tar.gz" -o SimpleFlask.tar.gz && \
	tar -xf SimpleFlask.tar.gz -C . && \
	mkdir /app && \
	mv SimpleFlask-1.0/* /app/ && \
	rm SimpleFlask.tar.gz && \
	rm -rf SimpleFlask-1.0 && \
	mv /app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

WORKDIR /app

CMD ["/usr/bin/supervisord"]
