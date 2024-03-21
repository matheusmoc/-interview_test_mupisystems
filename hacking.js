const caracFreq = string => {
    const frequencia = {};
    
    string.split('').forEach(caractere => frequencia[caractere] = (frequencia[caractere] || 0) + 1);

    let caractereMaisComum = '';
    let frequenciaMaxima = 0;

    Object.entries(frequencia).forEach(([caractere, freq]) => {
        if (freq >= frequenciaMaxima) {
            caractereMaisComum = caractere;
            frequenciaMaxima = freq;
        }
    });
    
    return caractereMaisComum;
}

console.log(caracFreq("aabbc")); // 'b'
console.log(caracFreq("banana")); // 'a'


const dElements = (array1, array2) => {
    return array1.filter(element => !array2.includes(element));
}

const array1 = [1, 2, 3, 4, 5];
const array2 = [3, 4, 5, 6, 7];

console.log(dElements(array1, array2)); //1, 2]


const isAnagram = (str1, str2) => {
    str1 = str1.replace(/ /g,'');
    str2 = str2.replace(/ /g,'');
    return [...str1].sort().join('') === [...str2].sort().join('');
};

//anagramas são palavrar com ordens das letras diferentes
const string1 = "listen";
const string2 = "silent";

console.log(isAnagram(string1, string2)); //true