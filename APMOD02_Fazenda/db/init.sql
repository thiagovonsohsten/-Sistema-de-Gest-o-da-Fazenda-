CREATE DATABASE IF NOT EXISTS fazenda_db;
USE fazenda_db;

CREATE TABLE Animais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    especie VARCHAR(50),
    idade INT
);

CREATE TABLE Funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    cargo VARCHAR(50)
);

CREATE TABLE Manejo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    funcionario_id INT,
    atividade VARCHAR(100),
    data DATE,
    FOREIGN KEY (animal_id) REFERENCES Animais(id),
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id)
);

-- Inserção de dados na tabela Animais
INSERT INTO Animais (nome, especie, idade) VALUES
('Bela', 'Vaca', 5), 
('Thor', 'Cavalo', 3), 
('Milly', 'Ovelha', 2),
('Max', 'Cavalo', 4), 
('Luna', 'Vaca', 6), 
('Bella', 'Ovelha', 1);

-- Inserção de dados na tabela Funcionarios
INSERT INTO Funcionarios (nome, cargo) VALUES
('José', 'Veterinário'), 
('Maria', 'Zootecnista'), 
('Carlos', 'Cuidador'),
('Ana', 'Veterinária'), 
('João', 'Cuidador'), 
('Fernanda', 'Zootecnista');

-- Inserção de dados na tabela Manejo
INSERT INTO Manejo (animal_id, funcionario_id, atividade, data) VALUES
(1, 1, 'Vacinação', '2023-01-01'), 
(2, 2, 'Ferrageamento', '2023-01-10'),
(3, 3, 'Alimentação', '2023-02-01'), 
(4, 1, 'Tratamento', '2023-02-15'),
(5, 2, 'Exame de Rotina', '2023-03-05'), 
(6, 3, 'Dieta Especial', '2023-04-20');
